from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)

    print(char_count)
    print(f"""
--- Begin report of {book_path} ---
{num_words} words found in the document
    """)
    for i in char_count:
        print(f"The '{i}' character was found {char_count[i]} times")
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
