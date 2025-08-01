# -*- coding: utf-8 -*-
# random password generator
# A simple and fast random password written in Python
# Inspired by an example found on Geeks for Geeks site.

# import functions
from random import choice
from string import ascii_letters, digits
from os import listdir

# Program requires to user how many characters must be password

while(True):
    try:
        num_chars = int(input("Enter the numerical length of password: "))
    except ValueError:
        print("Error, are allowed only integer.")
        continue
    break

while(True):
    print("What punctuation table would you use?\nType the number from follow list,\nleave empty and press ENTER for generic table.:")
    c=0
    file_dict = {}
    for i in listdir():
        if i.endswith(".tab") == True:
            c+=1
            file_dict[c] = i
    # show list of tab files
    for i in file_dict:
        print(f"    {i} -> {file_dict[i].rstrip(".tab")}")
    try:
        tabfile = int(input("Choice: "))
        if tabfile == "":
            with open("generic.tab") as f:
                punctuation = f.read()
            break

        with open(file_dict[tabfile]) as f:
            punctuation = f.read()
        break
    except KeyError:
        print("Invalid key, please try again.")

# Initialize chars list that will contains all possible alfanumeric and punctuation characters. Note: punctuation characters gets from tab file
chars = list(ascii_letters+digits+punctuation)

# initialize password list that will contains all password chars
password = []

# iteration cycle that choice single characters from chars list and append them at password list
for i in range(num_chars):
    password.append(choice(chars))
print(f"Password generated succesfully and it's follow\n   {"".join(password)}")
while True:
    q = input("Would you like to save in a file? (y/n): ").lower()
    if q == "y":
        with open("pagen.txt", "w") as f:
            print("".join(password), file=f)
        print("Done.")
        break
    elif q == "n":
        break
    print("Error, invalid answer")
input("Press ENTER to quit.")