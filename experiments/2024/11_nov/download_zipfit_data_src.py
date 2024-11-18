# from datasets import load_dataset

# def download_train_split(dataset_name, save_path=None):
#     """
#     Downloads only the 'train' split of a Hugging Face dataset.

#     Args:
#         dataset_name (str): The name of the dataset on Hugging Face (e.g., "UDACA/Code-Mixed-Dataset").
#         save_path (str, optional): Custom path to save the train split. Defaults to None, 
#                                    which uses the Hugging Face default cache directory.
#     """
#     print(f"Downloading 'train' split of dataset: {dataset_name}...")
    
#     # Load only the 'train' split
#     dataset = load_dataset(dataset_name, split="train")
    
#     # Save to custom path or Hugging Face cache
#     if save_path:
#         # Ensure the directory exists
#         import os
#         os.makedirs(save_path, exist_ok=True)
        
#         # Save as a JSONL file
#         file_path = f"{save_path}/train.jsonl"
#         dataset.to_json(file_path, lines=True)
#         print(f"'train' split saved to: {file_path}")
#     else:
#         print("'train' split downloaded to the default Hugging Face cache directory.")
    
#     print("Download complete!")

# if __name__ == "__main__":
#     # Specify the dataset name
#     dataset_name = "UDACA/Code-Mixed-Dataset"
    
#     # Optional: Specify a custom save path
#     # save_path = "./code_mixed_dataset"  # Change to your desired directory or set to None for default location
    
#     # Download the train split
#     download_train_split(dataset_name)

#%%
import requests
import os

def download_jsonl(url, save_path):
    """
    Downloads a JSONL file from a URL and saves it locally.

    Args:
        url (str): The URL of the JSONL file to download.
        save_path (str): The local path where the file will be saved.
    """
    print(f"Starting download from {url}...")
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP request errors
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Download complete! File saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # URL to the JSONL file
    dataset_url = "https://huggingface.co/datasets/UDACA/Code-Mixed-Dataset/resolve/main/combined_dataset.jsonl"
    
    # Local path to save the file
    save_path = os.path.expanduser("~/data/combined_dataset.jsonl")
    
    # Download the file
    download_jsonl(dataset_url, save_path)
