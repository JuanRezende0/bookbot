from stats import count_words
from stats import get_char_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dictionary = get_char_dictionary(text)
    print(f"{num_words} words found in the document")
    print(char_dictionary)

main()
