# Goal: get enough seqs from zipfits src dataset until we have 1M toks (using the gemma 2b tokenizer)
plan:
1. download src (automatic location that HF does) from https://huggingface.co/datasets/UDACA/Code-Mixed-Dataset/tree/main
2. 


```bash

conda activate shed
cd ~/SHED-Shapley-Based-Automated-Dataset-Refinement/src
bash ~/SHED-Shapley-Based-Automated-Dataset-Refinement/src/run_shed_4_zipfit.sh

```