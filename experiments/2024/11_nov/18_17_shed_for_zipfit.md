# Goal: get enough seqs from zipfits src dataset until we have 1M toks (using the gemma 2b tokenizer)
plan:
1. download src (automatic location that HF does) from https://huggingface.co/datasets/UDACA/Code-Mixed-Dataset/tree/main
2. 

in case direct install is needed but setup.py should work 
```bash
# pip install accelerate appdirs loralib bitsandbytes black black[jupyter] datasets fire sentencepiece gradio && pip install git+https://github.com/huggingface/peft.git && pip install git+https://github.com/huggingface/transformers.git
```

```bash

conda activate shed
cd ~/SHED-Shapley-Based-Automated-Dataset-Refinement/src
bash ~/SHED-Shapley-Based-Automated-Dataset-Refinement/src/run_shed_4_zipfit.sh

```

fetch from original shed:
```bash
# Step 1: Add the original repository as an upstream remote
# Only needed the first time. Skip this if 'upstream' is already configured.
git remote add upstream https://github.com/Lucidreamer9/SHED-Shapley-Based-Automated-Dataset-Refinement.git

# Step 2: Fetch the latest updates from the original repository
git fetch upstream

# Step 3: Merge or rebase updates from 'upstream/main' into your fork
# Use 'merge' to combine changes (simpler but might include merge commits)
git merge upstream/main

# If you prefer to rebase (keeps history clean, but more complex), uncomment the following line:
# git rebase upstream/main

# Step 4: Push the changes to your fork on GitHub (optional, to sync your online repository)
git push origin main
```

