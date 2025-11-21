def count_words(content):
    count = content.split()
    count = len(count)
    return (f"Found {count} total words")

def count_per_character(content):
    character_counts = {}
    words = content.split()
    for word in words:
        word = word.lower()
        length = len(word)
        for character in word:
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] =  1
    return (character_counts)
        

if __name__ == "__main__":
    sample_text = "Apple banana apricot berry"
    count_per_character(sample_text)