import json
import os

def convert_jsonl_to_json(jsonl_path, output_path):
    """
    Converts a JSONL file to a JSON file containing a list of dictionaries.

    Args:
        jsonl_path (str): Path to the input JSONL file.
        output_path (str): Path to save the output JSON file.
    """
    try:
        with open(jsonl_path, 'r', encoding='utf-8') as infile:
            data = [json.loads(line) for line in infile]
        data = data[:12]
        
        with open(output_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)

        print(f"Successfully converted {jsonl_path} to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define paths
    jsonl_path = os.path.expanduser("~/data/combined_dataset.jsonl")  # Update with your .jsonl path
    output_path = os.path.expanduser("~/data/combined_dataset_12.json")  # Save as a .json file

    # Convert the file
    convert_jsonl_to_json(jsonl_path, output_path)
