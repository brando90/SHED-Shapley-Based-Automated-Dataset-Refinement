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
