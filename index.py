import random

def printall():
    for i in range(5):
        print(i)

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

def get_random_number():
    return random.randint(1, 100)