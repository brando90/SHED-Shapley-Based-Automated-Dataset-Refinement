import json
import os
import sys

def convert_jsonl_to_json(jsonl_path, output_path, end = sys.maxsize):
    """
    Converts a JSONL file to a JSON file containing a list of dictionaries.

    Args:
        jsonl_path (str): Path to the input JSONL file.
        output_path (str): Path to save the output JSON file.
    """
    try:
        print(f'{end=}')
        print(f'{jsonl_path=}')
        with open(jsonl_path, 'r', encoding='utf-8') as infile:
            data = []
            for line in infile:
                if len(data) >= end:
                    assert len(data) == end
                    break
                else:
                    data.append(json.loads(line))
        print(f'{len(data)=}')
        print(data)
        
        print(f'{output_path=}')
        with open(output_path, 'w', encoding='utf-8') as outfile:
            print(f'{len(data)=}')
            json.dump(data, outfile, indent=4, ensure_ascii=False)
        with open(output_path, 'r', encoding='utf-8') as infile:
            data_written = json.load(infile)
            print(f'{len(data_written)=}')
            assert len(data_written) == len(data)
        file_size = os.path.getsize(output_path) / (1024 ** 3)
        print(f'{file_size=}')

        print(f"--> Successfully converted {jsonl_path} to {output_path}")
        return data
    except Exception as e:
        print(f"----> ERROR: An error occurred: {e}")
        return []

if __name__ == "__main__":
    # Convert full combine ds to json (shed needs this) 
    print('-- Convert full combine ds to json (shed needs this) ')
    jsonl_path = os.path.expanduser("~/data/combined_dataset.jsonl")  # Update with your .jsonl path
    output_path = os.path.expanduser("~/data/combined_dataset.json")  # Save as a .json file
    data = convert_jsonl_to_json(jsonl_path, output_path)
    assert len(data) > 12

    # Convert subset combine ds to json (shed needs this) to debug
    print('-- Convert subset combine ds to json (shed needs this) ')
    end: int = 12 # >=10 shed requires
    jsonl_path = os.path.expanduser("~/data/combined_dataset.jsonl")  # Update with your .jsonl path
    output_path = os.path.expanduser(f"~/data/combined_dataset_{end}.json")  # Save as a .json file
    data = convert_jsonl_to_json(jsonl_path, output_path, end=end)
    assert len(data) == 12

    print('\n--Done!\a\n')
