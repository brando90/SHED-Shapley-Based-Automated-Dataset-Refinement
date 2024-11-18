import json
from transformers import AutoTokenizer

# Load the Gemma 2B tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")

# Path to your JSON file
json_file_path = 'path_to_your_file.json'

# Initialize variables
total_tokens = 0
target_token_count = 1_000_000
selected_texts = []

# Read and process the JSON file
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    for entry in data:
        text = entry.get('text', '')
        if text:
            # Tokenize the text
            tokens = tokenizer.tokenize(text)
            num_tokens = len(tokens)
            # Check if adding this text exceeds the target token count
            if total_tokens + num_tokens > target_token_count:
                break
            # Add the text to the selected list
            selected_texts.append(text)
            total_tokens += num_tokens

print(f"Total tokens accumulated: {total_tokens}")
print(f"Number of texts selected: {len(selected_texts)}")
