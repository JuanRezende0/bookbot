from stats import count_words
from stats import get_char_dictionary
from stats import sorting_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dictionary = get_char_dictionary(text)
    sorted_list = sorting_dictionary(char_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f'{i["char"]}: {i["num"]}')
    print("============= END ===============")

main()
