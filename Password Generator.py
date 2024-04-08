# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:14:46 2024

@author: ATANU
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Length must be greater than zero.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
