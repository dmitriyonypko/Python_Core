"""Task 4:
Your order, please
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""


some_string = input("Enter the string: ")
dict_words = {}
result = ''


list_words = some_string.split()
for word in list_words:
    for item in word:
        if item.isdigit():
            dict_words[item] = word
list_keys = list(dict_words.keys())
list_keys.sort()
for dig in list_keys:
    result += dict_words[dig] + ' '
result = result.strip()

print(some_string, '\n')
print(result)
