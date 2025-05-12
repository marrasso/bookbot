def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}
    # Convert text to lowercase and count each character
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list
