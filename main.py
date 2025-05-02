import sys
#imports
from stats import get_num_words
from stats import get_num_characters
from stats import sort_chars_by_count

def get_book_text(filepath):
    with open(filepath) as f:
        word = f.read()
        return word

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    
    # Get counts
    word_count = get_num_words(book_text)
    char_counts = get_num_characters(book_text)
    sorted_chars = sort_chars_by_count(char_counts)

    # Print report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Print character count section
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    # Print footer
    print("============= END ===============")

if __name__ == "__main__":
    main()