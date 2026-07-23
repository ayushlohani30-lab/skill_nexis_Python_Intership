# Word Counter from Text File

def count_file_stats(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            line_count = len(lines)
            word_count = 0
            char_count = 0
            
            for line in lines:
                words = line.split()
                word_count += len(words)
                char_count += len(line)  # Includes spaces and newlines
            
            print("\n=== FILE ANALYSIS RESULTS ===")
            print(f"File Name: {file_path}")
            print(f"Total Lines     : {line_count}")
            print(f"Total Words     : {word_count}")
            print(f"Total Characters: {char_count}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Demo Usage: Creates a sample file if it doesn't exist, then reads it
filename = "sample.txt"

# Creating a test file for demonstration
with open(filename, 'w', encoding='utf-8') as f:
    f.write("Hello world!\nWelcome to Python Internship Week 2.\nCounting lines, words, and characters is easy.")

print(f"Sample file '{filename}' created for testing.")
count_file_stats(filename)