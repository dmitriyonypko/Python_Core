"""
Task 1: Count the number of Duplicates
Write a function that will return the count of distinctcase-insensitive alphabetic characters
and numeric digits that occur more than once in the input string.
The input string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""


some_string = input("Enter the string: ")


def count_chars(some_string):
    some_string = some_string.lower()
    count_chars = 0
    helper_string = ""
    for char in some_string:
        if some_string.count(char) > 1:
            helper_string += char
            if helper_string.count(char) == 1:
                count_chars += 1
    return count_chars

print("Count chars:", count_chars(some_string))
