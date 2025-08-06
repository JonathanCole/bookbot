def word_count(text):
    count = text.split()
    return len(count)

def char_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def list_sort(dict):
    sorted_list = []
    for each in dict:
        temp = {"char": each, "num": dict[each]} 
        sorted_list.append(temp)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

