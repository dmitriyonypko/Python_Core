"""Task 3:
Shortest Word
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
Examples
"bitcoin take over the world maybe who knows perhaps" --> 3)
"turns out random test cases are easier than writing out basic ones" --> 3)
"lets talk about javascript the best language" --> 3)
"i want to travel the world writing code one day" --> 1)
"Lets all go on holiday somewhere very cold" --> 2)
"""


import re


some_string = input("Enter the string: ").lower()
some_string = re.sub(r'[,\.\?!-:;]','', some_string)


list_words = some_string.split()
count_words = []

for word in list_words:
    count_words.append(len(word))

count_words.sort()

print("The length of the shortest word(s):", count_words[0])
