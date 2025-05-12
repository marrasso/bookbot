import sys
from stats import count_words, count_chars, sort_chars

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filepath} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {str(e)}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = count_chars(text)
    sorted_chars = sort_chars(char_count)
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
