from stats import word_count
from stats import char_count
from stats import list_sort
import sys

if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def prepend(count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

def postpend():
    print("============= END ===============")

def main():
    count = word_count(get_book_text(sys.argv[1]))
    chars = get_book_text(sys.argv[1])
    prepend(count)
    for each in list_sort(char_count(chars)):
        if each["char"].isalpha():
            print(f"{each["char"]}: {each["num"]}")
    postpend()

main()