import json
import os

def convert_jsonl_to_json(jsonl_path, output_path, end = None):
    """
    Converts a JSONL file to a JSON file containing a list of dictionaries.

    Args:
        jsonl_path (str): Path to the input JSONL file.
        output_path (str): Path to save the output JSON file.
    """
    try:
        print(f'{end=}')
        with open(jsonl_path, 'r', encoding='utf-8') as infile:
            data = [json.loads(line) for line in infile]
        if end is None: # if end is None download all data
            pass
        else:
            data = data[:end]
        
        with open(output_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)

        print(f"--> Successfully converted {jsonl_path} to {output_path}")
    except Exception as e:
        print(f"----> ERROR: An error occurred: {e}")

if __name__ == "__main__":
    # Convert full combine ds to json (shed needs this) 
    print('-- Convert full combine ds to json (shed needs this) ')
    jsonl_path = os.path.expanduser("~/data/combined_dataset.jsonl")  # Update with your .jsonl path
    output_path = os.path.expanduser("~/data/combined_dataset.json")  # Save as a .json file
    convert_jsonl_to_json(jsonl_path, output_path)

    # Convert subset combine ds to json (shed needs this) to debug
    print('-- Convert subset combine ds to json (shed needs this) ')
    end: int = 12 # >=10 shed requires
    jsonl_path = os.path.expanduser("~/data/combined_dataset.jsonl")  # Update with your .jsonl path
    output_path = os.path.expanduser(f"~/data/combined_dataset_{end}.json")  # Save as a .json file
    convert_jsonl_to_json(jsonl_path, output_path)

    print('\n--Done!\a\n')
