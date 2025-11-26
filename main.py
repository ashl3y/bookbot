import sys
from stats import count_words, count_per_character, build_loop, sort_on

def get_book_text(book_path):
    with open(book_path) as file:
        content = file.read()
    return content
    
def main(book_path):
    content = get_book_text(book_path)
    return(content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        book_link = sys.argv[1]
        content = main(book_link)
        word_result = count_words(content)
        dict = count_per_character(content)
        result = build_loop(dict)
        result.sort(key=sort_on, reverse=True)
        
        #output report
        print("========== BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("---------- Word Count ---------")
        print(word_result)
        print("---------- Character Count ----")
        for items in result:
            print(f"{items["char"]}: {items["num"]}")
        print("========== END =========")
        #print(sys.argv)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)