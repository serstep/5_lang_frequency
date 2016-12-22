#!/usr/bin/python3.4
import sys
import re
from collections import Counter  


def load_data(filepath):
    with open(filepath) as file_with_text:
        text = file_with_text.read()

    return text


def get_most_frequent_words(text):
    required_words_number = 10
    regexp = "[^\s\d.,-:'\"`;)(?!&]+"
    words_list = re.findall(regexp, text.lower())
    return Counter(words_list).most_common(required_words_number)


if __name__ == '__main__':
    try: 
        text = load_data(sys.argv[1])
    except:
        print("Невозможно прочитать текстовый файл файл")
        exit(1)

    for i in get_most_frequent_words(text):
        print("Слово:", i[0], "Количество:", i[1])
