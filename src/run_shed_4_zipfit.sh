#!/bin/bash

# Define parameters as environment variables for easy modification
# Small values for debugging
export NUMBER_OF_CLUSTERS=10       # Small number of clusters (original: 3000)
export NUMBER_OF_FINALSET=20       # Small final dataset size (original: 5000)
export OUTER_LOOP_LIMIT=2          # Small number of outer loop iterations (original: 20)
export INNER_LOOP_LIMIT=5          # Small number of inner loop iterations (original: 50)
export BATCH_SIZE=16               # Reduced batch size for debugging (original: 128)
export CUT_OFF_LEN=256             # Reduced token cutoff length for faster processing (original: 1024)
export NUM_EPOCHS=1                # Fewer epochs for debugging (original: 3)
export OUT_NUM=5                   # Smaller random output samples (original: 60)
export LORA_R=4                    # Small value for LoRA rank (original: 128)
export LORA_ALPHA=4                # Small value for LoRA alpha (original: 256)

# Large original values (commented for reference)
# export NUMBER_OF_CLUSTERS=3000
# export NUMBER_OF_FINALSET=5000
# export OUTER_LOOP_LIMIT=20
# export INNER_LOOP_LIMIT=50
# export BATCH_SIZE=128
# export CUT_OFF_LEN=1024
# export NUM_EPOCHS=3
# export OUT_NUM=60
# export LORA_R=128
# export LORA_ALPHA=256

# Activate conda environment for shed
# pip install -U sentence-transformers |
conda activate shed 

# Path configurations
ORIGINAL_DATASET="$HOME/data/combined_dataset.jsonl"  # Path to the downloaded dataset
ORIGINAL_DATASET="$HOME/data/combined_dataset.json"  # Path to the downloaded dataset
ORIGINAL_DATASET="$HOME/data/combined_dataset_12.json"  # Path to the downloaded dataset
DEV_DATA_PATH="./workspace/dev_data.json"            # Path for dev data (ensure this exists)

# Ensure necessary directories exist
for dir in "workspace" "output" "final_dataset"; do
  if [ ! -d "$dir" ]; then
    mkdir "$dir"
    echo "Directory '$dir' created."
  else
    echo "Directory '$dir' already exists."
  fi
done

# Step 1: Run clustering
echo "Clustering the original dataset..."
python cluster_sen_tran.py "${ORIGINAL_DATASET}" "${NUMBER_OF_CLUSTERS}" || exit 1
python txt_json.py ${NUMBER_OF_CLUSTERS} || exit 1

# Step 2: Run iteration_shapley.sh
echo "Preparing for Shapley value calculation..."
for i in $(seq 1 $OUTER_LOOP_LIMIT); do
  data_path="./workspace/cluster_center_${NUMBER_OF_CLUSTERS}_${i}.json"
  count_fine_path="./workspace/count_file_${NUMBER_OF_CLUSTERS}_${i}.txt"
  temp_save_filepath="./workspace/randomout_${NUMBER_OF_CLUSTERS}_${i}.json"

  for j in $(seq 1 $INNER_LOOP_LIMIT); do
    python -u finetune_fixseed.py \
      --base_model yahma/llama-7b-hf \
      --batch_size $BATCH_SIZE \
      --cutoff_len $CUT_OFF_LEN \
      --micro_batch_size 8 \
      --num_epochs $NUM_EPOCHS \
      --add_lora True \
      --lora_r $LORA_R \
      --lora_alpha $LORA_ALPHA \
      --save_strategy no \
      --max_new_token 4 \
      --data_path "$data_path" \
      --dev_data_path "$DEV_DATA_PATH" \
      --verbose False \
      --resume_from_checkpoint None \
      --count_fine_path "$count_fine_path" \
      --output_dir "./output" || exit 1

    python random_out.py \
      --out_num $OUT_NUM \
      --out_filepath "$data_path" \
      --temp_save_filepath "$temp_save_filepath" || exit 1
  done
done

# Step 3: Calculate Shapley values
echo "Calculating Shapley values..."
python calculate_s.py "${NUMBER_OF_CLUSTERS}" || exit 1

# Step 4: Sample the final selected dataset
echo "Sampling the final selected dataset using QOCS and QWCS..."
python sample_QOCS.py "${NUMBER_OF_CLUSTERS}" "${NUMBER_OF_FINALSET}" || exit 1
python sample_QWCS.py "${NUMBER_OF_CLUSTERS}" "${NUMBER_OF_FINALSET}" || exit 1

# Clean up workspace and outputs (optional)
WORKSPACE_DIR="./workspace"
OUTPUT_DIR="./output"
rm -rf "${WORKSPACE_DIR}"/* || exit 1
rm -rf "${OUTPUT_DIR}"/* || exit 1
echo "Debug process completed successfully."
