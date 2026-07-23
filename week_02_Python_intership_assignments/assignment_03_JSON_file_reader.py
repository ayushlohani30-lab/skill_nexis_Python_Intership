# JSON File Reader

import json

def read_and_format_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            print("\n=== FORMATTED JSON OUTPUT ===")
            # json.dumps with indent=4 pretty-prints the JSON structure
            formatted_output = json.dumps(data, indent=4)
            print(formatted_output)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Demo Usage: Creates a sample JSON file first for testing
filename = "student_data.json"

sample_json = {
    "organization": "Skill Nexis",
    "course": "Python Programming Internship",
    "student": {
        "id": 101,
        "name": "Ayush",
        "skills": ["Python", "Git", "Data Analysis"],
        "active_enrollment": True
    }
}

# Write dummy JSON data
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(sample_json, f, indent=4)

print(f"Sample JSON file '{filename}' created for testing.")
read_and_format_json(filename)