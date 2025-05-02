def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_num_characters(book_text):
    characters = {}
    for character in book_text:
        lowercase_character = character.lower()
        if lowercase_character in characters:
            characters[lowercase_character] += 1
        else:
            characters[lowercase_character] = 1
    return characters

def sort_chars_by_count(characters):
    sorted_chars = []
    for char, count in characters.items():
        sorted_chars.append({"char": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]
    
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars