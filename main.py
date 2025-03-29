import sys
from stats import get_num_words, get_num_char, get_sort_char

def get_book_text(book):
    with open(book) as f:
        file_content = f.read()
    return file_content

def book_exist(book_path):
    if len(book_path) == 2:
        return book_path[1]
    raise SystemExit("Usage: python3 main.py <path_to_book>")

def main():
    try:
        book = book_exist(sys.argv)
        text = get_book_text(book)
        num_words = get_num_words(text)
        char_num = get_num_char(text)
        sort_char = get_sort_char(char_num)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char_dict in sort_char:
            if char_dict["char"].isalpha():
                print(f"{char_dict["char"]}: {char_dict["num"]}")
        print("============= END ===============")
    except Exception as e:
        print(e)
main()
