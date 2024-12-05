import sys
import random

# the function to get unique words longer than 10 characters
def find_long_words(file_path):
    try:
        # opens the file and read it
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # split the text snd filter out words
        words = text.split()
        long_words = [word.lower() for word in words if len(word) > 10]
        
        # creates a set to get unique words
        unique_long_words = list(set(long_words))
        
        return unique_long_words
    
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found. Please check the path.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# main program
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 program.py <file_path>")
    else:
        file_path = sys.argv[1]
        long_words = find_long_words(file_path)
        
        # check if we have enough words to pick 10
        if len(long_words) < 10:
            print("Not enough unique words longer than 10 characters were found.")
            print("Here are the words found:")
            print(long_words)
        else:
            # picked 10 random unique words
            random_words = random.sample(long_words, 10)
            print("Here are 10 random unique words over 10 characters long:")
            for word in random_words:
                print(word)
