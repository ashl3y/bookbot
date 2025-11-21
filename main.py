from stats import count_words, count_per_character

def get_book_text(book_path):
    with open(book_path) as file:
        content = file.read()
    return content
    
def main(book_path):
    content = get_book_text(book_path)
    return(content)

if __name__ == "__main__":
    content = main("books/frankenstein.txt")
    result = count_words(content)
    dict = count_per_character(content)
    print(result, dict)
