"""Task 1:
Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
"""


some_string = "It's Pig latin, is cool. !"


def pigIt(string):
    result = []
    for word in string.split():
        if word.isalpha():
            result.append(word[1:] + word[0] + 'ay')
        elif len(word) == 1:
            result.append(word)
        else:
            result.append(word[1:-1] + word[0] + 'ay' + word[-1])

    return ' '.join(result)


print(some_string)
print(pigIt(some_string))
