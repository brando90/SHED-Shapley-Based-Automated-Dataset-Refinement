# SHED-Shapley-Based-Automated-Dataset-Refinement

paper link: https://arxiv.org/abs/2405.00705

Before running the project, please make sure that you have installed the required dependencies.

Please prepare your original dataset and make sure it's in the right format.
Please note that in order to reduce the computational overhead when calculating the Shapley value, we use 1444 instances (devdata_1444) in MMLU to evaluate the model performance. If you target other tasks, please modify the corresponding evaluation part in finetune_fixseed.py.
The scripts in the project have been integrated into the run.sh script, which handles the entire workflow. Ensure that all file paths are correct. The final selected dataset will be saved in final_dataset.

The base model we use is llama-7b, ensure that you have sufficient computational resources to run the models, especially during the Shapley value calculation and model fine-tuning steps.
The path and format of the original dataset must comply with the scripts' requirements.

## Install & Clone our Shed repo & Nvhtop
```bash
# Nvhtop 
pip3 install nvidia-htop
alias nvhtop='nvidia-htop.py --color -l 100'

# Clone
cd ~
git clone git@github.com:brando90/SHED-Shapley-Based-Automated-Dataset-Refinement.git

# Create shed env
conda create -n shed python=3.11 -y
conda activate shed
conda activate shed
# conda remove --all --name shed

# Install deps + dev install
# pip install accelerate appdirs loralib bitsandbytes black black[jupyter] datasets fire sentencepiece gradio && pip install git+https://github.com/huggingface/peft.git && pip install git+https://github.com/huggingface/transformers.git
pip install -e ~/SHED-Shapley-Based-Automated-Dataset-Refinement
```

## Download our src code data & put it into SHED format
```bash
# download raw jsonl file from hf (elyas had a bug so it has to be the jsonl raw file)
python ~/SHED-Shapley-Based-Automated-Dataset-Refinement/experiments/2024/11_nov/download_zipfit_data_jsonl_src_ds.py
# convert jsonl file to json format for SHED
python ~/SHED-Shapley-Based-Automated-Dataset-Refinement/experiments/2024/11_nov/transform_src_ds_from_jsonl_to_json.py
```

## Run SHED on our ZIP-FIT code data set
To run BM's shed, run the cmds bellow: 
```bash
conda activate shed
cd ~/SHED-Shapley-Based-Automated-Dataset-Refinement/src
bash ~/SHED-Shapley-Based-Automated-Dataset-Refinement/src/run_shed_4_zipfit.sh
```
