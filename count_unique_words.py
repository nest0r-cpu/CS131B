import sys
import string

def estimate_unique_words(filepath):
    """
    Estimates the number of unique words in the file specified by the filepath.
    """
    try:
        # Opens file and read it
        file = open(filepath, 'r', encoding='utf-8')
        text = file.read()
        file.close()

        # Removes punctuation and converts text to lowercase
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator).lower()
        
        # Splits the text into words
        words = text.split()

        # Tracks only unique words
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)

        # Prints unique word count
        print(f"The file '{filepath}' contains {len(unique_words)} unique words.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{filepath}'.")
    except UnicodeDecodeError:
        print(f"Error: The file '{filepath}' is not encoded in UTF-8.")
    except Exception as e:
        print(f"Error: {e}")

# Checks for filename arguments
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python estimate_unique_words.py <file_path>")
    else:
        file_path = sys.argv[1]
        estimate_unique_words(file_path)
