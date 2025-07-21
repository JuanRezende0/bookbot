def count_words(book_text):
    words = book_text.split()
    return len(words)

def get_char_dictionary(book_text):
    lowered_text = book_text.lower()
    char_dictionary = {}
    for char in lowered_text:
        is_char_present = char in char_dictionary
        if is_char_present == False:
            char_dictionary[char] = 1
        else:
            char_dictionary[char] += 1
    return char_dictionary

def sort_on(items):
    return items["num"]

def sorting_dictionary(dictionary):
    list = []
    for key in dictionary:
        is_true = key.isalpha()
        if is_true == True:
            char_dic= {"char": key, "num": dictionary[key]}
            list.append(char_dic)
    list.sort(reverse=True, key=sort_on)
    return list
