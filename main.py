from stats import *
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(num_words, dict_of_chars):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in dict_of_chars.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    num_words = get_word_count(file_contents)
    dict_of_chars = sort_dict(get_count_of_chars(file_contents))

    print_report(num_words, dict_of_chars)

main()