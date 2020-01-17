"""Task 3:
Complete the function scramble(str1, str2)
that returns true if a portion of str1 characters can be rearranged to match str2,
otherwise returns false.

Notes:
Only lower case letters will be used (a-z).
No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.

Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""


str1 = 'cedewaraaossoqqyt'
str2 = 'codewars'


def scramble(str1, str2):
    """Returns true if a portion of str1 characters can be rearranged to match str2,
    otherwise returns false."""
    d = {i:str2.count(i) for i in str2}
    d2 = {i:str1.count(i) for i in str1 if i in d}
    return len(d2) == len(d)


print(scramble(str1, str2))
