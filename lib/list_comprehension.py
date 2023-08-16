#!/usr/bin/env python3


def return_evens(num_list):
    isEven = [n for n in num_list if n % 2 == 0]
    return isEven
    pass


def print_evens(num_list):
    checkEvens = return_evens(num_list)
    print(checkEvens)


print_evens([0, 1, 3, 5, 7, 8, 9])


def make_exclamation(sentence_list):
    exclamation_list = [word + "!" for word in sentence_list]
    return exclamation_list
    pass


exclamated_list = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(exclamated_list)
