"""
refs:
    - setup tools: https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#using-find-or-find-packages
    - https://stackoverflow.com/questions/70295885/how-does-one-install-pytorch-and-related-tools-from-within-the-setup-py-install
"""
from setuptools import setup
from setuptools import find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SHED-Shapley-Based-Automated-Dataset-Refinement',  # project name
    version='0.0.1',
    description="Brandos Shed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="TODO",
    author='Brando Miranda',
    author_email='brandojazz@gmail.com',
    python_requires='>=3.11',
    license='Apache 2.0',

    packages=find_packages(include=['src', 'src.*', 'utils', 'utils.*']),
    package_dir={
        'src': 'src',
        'utils': 'utils'
    },

    install_requires=[
        "accelerate",
        "appdirs",
        "loralib",
        "bitsandbytes",
        "black",
        "black[jupyter]",
        "datasets",
        "fire",
        "gradio",
        "sentencepiece",
        "peft==0.9.0", 
        "transformers",
        "requests",
        'sentence-transformers',
        'nvidia-htop',
    ]

    # for pytorch see doc string at the top of file
    # install_requires=[
    #     # 'fire',
    #     # 'dill',
    #     # # 'networkx>=2.5',
    #     # 'scipy',
    #     # 'scikit-learn',
    #     # 'lark-parser',
    #     # 'tensorboard',
    #     # 'pandas',
    #     # 'progressbar2',
    #     # 'requests',
    #     # 'aiohttp',
    #     # 'numpy',
    #     # 'plotly',
    #     # 'wandb',
    #     # 'matplotlib',
    #     # 'nvidia-htop',
    #     # 'openai',
    #     # 'anthropic',
    #     # 'jsonlines',
    #     # # 'statsmodels'
    #     # # 'statsmodels==0.12.2'
    #     # # 'statsmodels==0.13.5'
    #     # # - later check why we are not installing it...
    #     # 'seaborn',
    #     # # 'nltk'
    #     # 'twine',
    #     # 'dspy-ai',
    #     # 'ragatouille',
    #     # 'torch',  # here so it's there for default but if using vllm see bellow or readme.md
    #     # # 'torchvision',
    #     # # 'torchaudio',
    #     # 'trl',
    #     # 'transformers',
    #     # 'peft',
    #     # 'accelerate',
    #     # 'datasets',
    #     # 'bitsandbytes',
    #     # 'evaluate',
    #     # 'einops',
    #     # 'sentencepiece', # needed llama2 tokenizer
    #     # 'zstandard', # needed for eval of all the pile

    #     # def does not work for mac
    #     # # -- ref: https://github.com/vllm-project/vllm/issues/2747 
    #     # pip install torch==2.2.1
    #     # pip install vllm==0.4.1
    #     # 'torch==2.2.1',
    #     # 'vllm==0.4.1', 
    #     # # --

    #     # # mercury: https://github.com/vllm-project/vllm/issues/2747
    #     # 'dspy-ai',
    #     # # 'torch==2.1.2+cu118',  # 2.2 net supported due to vllm see: https://github.com/vllm-project/vllm/issues/2747
    #     # 'torch==2.2.2',  # 2.2 net supported due to vllm see: https://github.com/vllm-project/vllm/issues/2747
    #     # # 'torchvision',
    #     # # 'torchaudio',
    #     # # 'trl',
    #     # 'transformers',
    #     # 'accelerate',
    #     # # 'peft',
    #     # # 'datasets==2.18.0', 
    #     # 'datasets',  
    #     # 'evaluate', 
    #     # 'bitsandbytes',
    #     # # 'einops',
    #     # # 'vllm==0.4.0.post1', # my gold-ai-olympiad project uses 0.4.0.post1 ref: https://github.com/vllm-project/vllm/issues/2747

    #     # # ampere
    #     # 'dspy-ai',
    #     # # 'torch==2.1.2+cu118',  # 2.2 not supported due to vllm see: https://github.com/vllm-project/vllm/issues/2747
    #     # # 'torch==2.1.2',  # 2.2 not supported due to vllm see: https://github.com/vllm-project/vllm/issues/2747
    #     # # 'torch==2.2.1',  # 2.2 not supported due to vllm see: https://github.com/vllm-project/vllm/issues/2747
    #     # 'torch==2.2.1',  # 2.2 not supported due to vllm see: https://github.com/vllm-project/vllm/issues/2747
    #     # # 'torchvision',
    #     # # 'torchaudio',
    #     # # 'trl',
    #     # # 'transformers==4.39.2',
    #     # 'transformers>=4.40',
    #     # 'accelerate==0.29.2',
    #     # # 'peft',
    #     # # 'datasets==2.18.0', 
    #     # 'datasets==2.14.7',  
    #     # 'evaluate==0.4.1', 
    #     # 'bitsandbytes== 0.43.0',
    #     # 'einops',
    #     # 'flash-attn>=2.5.8',
    #     # 'vllm==0.4.1', # my gold-ai-olympiad project uses 0.4.0.post1 ref: https://github.com/vllm-project/vllm/issues/2747
    #     # # pip install -q -U google-generativeai
    # ]
)

