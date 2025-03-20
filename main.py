import sys
from stats import get_num_words

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)

    print(char_count)
    print(f"""
--- Begin report of {book_path} ---
{num_words} words found in the document
    """)
    for i in char_count:
        print(f"{i}: {char_count[i]}")
    print("--- End report ---")

def get_char_count(text):
    letter_count = {}
    for char in text:
        lowercase = char.lower()
        if lowercase.isalpha():
            if lowercase in letter_count:
                letter_count[lowercase] += 1
            else:
                letter_count[lowercase] = 1
    return letter_count
        
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
