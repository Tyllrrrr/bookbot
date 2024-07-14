def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    print(text)

    count = word_count(book_path)
    if count != -1:
        print(f"Number of words: {count}")

    char_count = count_characters(text)
    print(f"Character Counts: '{char_count}'")

def book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(book_path):
    try:
        with open(book_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return ""
    except IOError as e:
        print(f"Error: Could not read file '{file_path}': {e}")
        return ""
    
def count_characters(text):
    char_count = {}
    lowered_text = text.lower()
    
    for char in lowered_text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

main()