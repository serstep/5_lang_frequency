#!/usr/bin/python3.4
import sys
import re

def load_data(filepath):
    text = ""
    with open(filepath) as file:
        text = file.read()

    return text

def get_most_frequent_words(text):
    regexp = "[^\s\d.,-:'\"`;)(?!&]+"
    corpus = re.findall(regexp, text)

    required_words_number = 10
    frequency_table = dict()

    for i in corpus:
        if frequency_table.get(i) is None:
            frequency_table[i] = 1
        else:
            frequency_table[i] += 1

    most_frequent_words = list()

    for i in range(required_words_number):
        most_frequent_word = max(frequency_table, key=lambda w: frequency_table[w], default=None)

        most_frequent_words.append(most_frequent_word)
        frequency_table.pop(most_frequent_word)

    return most_frequent_words


if __name__ == '__main__':
    text = ""
    try: 
        text = load_data(sys.argv[1])
    except:
        print("Невозможно прочитать файл.")
        exit(0)

    for i in get_most_frequent_words(text):
        print(i)
