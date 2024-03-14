"""

MC Question:
What is the output of the following code:
    print(9//2)
Options:
A)4.0
B)Error
C)4
D)4.5

Answer: C


===============================
Programming question:


Write a function that returns how many vowels are in a word.


Possible solution:
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    index = 0

    while index < len(word):
            if word[index] in vowels:
                count += 1
            index += 1
    return count
"""

