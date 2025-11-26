def count_words(content):
    count = content.split()
    count = len(count)
    return (f"Found {count} total words")

def count_per_character(content):
    character_counts = {}
    words = content.split()
    for word in words:
        word = word.lower()
        for character in word:
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] =  1
    return (character_counts)

def sort_on(item):
    return item["num"]


def build_loop(sample_text):
    result = []
    entry = {}
    for ch, count in sample_text.items():
        if ch.isalpha():
            entry = {"char": ch, "num": count}
            result.append(entry) 
    return result     

if __name__ == "__main__":
    sample_text = "Apple banana apricot berry"
    count = count_per_character(sample_text)
    result = build_loop(count)
    result.sort(key=sort_on, reverse=True)
    print(result)