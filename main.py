import sys
from stats import count_words,get_book_text,count_characters,sort_dict
def main():
    if(len(sys.argv) == 1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    file_contents = get_book_text(path)
    num_words = count_words(file_contents)
    tmp = sort_dict(count_characters(file_contents))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in tmp:
        c = i['char']
        cnt = i['num']
        print(f"{c}: {cnt}")
    print("============= END ===============")
main()
