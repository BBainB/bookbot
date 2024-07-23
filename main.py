def main(book):
    book_path = book
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_character_count(text)
    print(f"{num_words} words found in the document")
    print(letter_count)
    print(organized_dict(letter_count))

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_character_count(string):
    letter_holder = {}
    
    for word in string:
        for letter in word:
            letter = letter.lower()
            if letter in letter_holder:
                letter_holder[letter] += 1
            else:
                letter_holder[letter] = 1
    return(letter_holder)

def organized_dict(dict_letters):
    sorted_items = sorted(dict_letters.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = {key: value for key, value in sorted_items}
    for key, value in dict_letters.items():
        print(f"This is the {key} and this is the {value}.")

def organized_dict(dict_letters):
    sorted_items = sorted(dict_letters.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = {key: value for key, value in sorted_items}
    for key, value in sorted_dict.items():
        print(f"This is the {key} and this is the {value}.")


main("books/frankenstein.txt")