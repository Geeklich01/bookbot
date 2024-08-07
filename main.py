def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    characters_dictionary = count_characters(text)
    dictionaries_list = dict_2_list(characters_dictionary)
    dictionaries_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print()
    for item in dictionaries_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")

def count_words(book: str) -> int:
    words = book.split()
    return len(words)

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()
    
def count_characters(book: str) -> dict:
    lowered_string = book.lower()
    dictionary = {}
    for character in lowered_string:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary


def dict_2_list(dictionary: dict) -> list:
    result = []
    for item in dictionary.items():
        result.append({"char": item[0], "num": item[1]})
    return result

def sort_on(dictionary: dict) -> int:
    return dictionary["num"]

if __name__ == "__main__":
    main()
