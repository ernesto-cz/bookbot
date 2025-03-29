
def get_num_words(book_text):
    txt_lst= book_text.split()
    return len(txt_lst) 

def get_num_char(book_text):
    char_set = set()
    char_num = dict()
    to_lower = book_text.lower()
    for char in to_lower:
        if char not in char_set:
            char_set.add(char)
            char_num[char] = to_lower.count(char)
    return char_num

'''
def sort_on(dict):
    return dict["num"]

    def get_sort_char(char_num):
    char_num_lst = []
    for key, value in char_num.items():
        char_num_lst.append(({"char": key, "num":value}))
    char_num_lst.sort(key=sort_on)
    return char_num_lst
'''

"""
def get_sort_char(char_num):
    char_num_lst = []
    for key, value in char_num.items():
        char_num_lst.append((key, value))
    print(sorted(char_num_lst,key=lambda char:char[1], reverse=True))
"""
def get_sort_char(char_num):
    char_num_lst = []
    for key, value in char_num.items():
        char_num_lst.append({"char":key, "num":value})
    char_num_lst.sort(key=lambda char: char["num"], reverse=True)
    return char_num_lst
