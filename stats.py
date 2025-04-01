def get_word_count(file_contents: str):
    return len(file_contents.split())

def get_count_of_chars(file_contents: str):
    list_of_chars = {}
    for char in file_contents:
        if char.lower() in list_of_chars:
            list_of_chars[char.lower()] += 1
        else:
            list_of_chars[char.lower()] = 1
    return list_of_chars

def sort_dict(dict_of_chars: dict):
    items = list(dict_of_chars.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return dict(items)