"""Task 4:
In order to prove it's success and gain funding,
the wilderness zoo needs to prove to environmentalists that it has x number of mating pairs of bears.

You must check within string (s) to find all of the mating pairs,
and return a string containing only them. Line them up for inspection.

Rules: Bears are either 'B' (male) or '8' (female),
Bears must be together in male/female pairs 'B8' or '8B',
Mating pairs must involve two distinct bears each ('B8B' may look fun, but does not count as two pairs).

Return an array containing a string of only the mating pairs available. e.g:

'EvHB8KN8ik8BiyxfeyKBmiCMj' ---> 'B88B' (empty string if there are no pairs)

and true if the number is more than or equal to x, false if not:

(6, 'EvHB8KN8ik8BiyxfeyKBmiCMj') ---> ['B88B', false];

x will always be a positive integer, and s will never be empty

7, '8j8mBliB8gimjB8B8jlB' --->  ["B8B8B8",False]
3, '88Bifk8hB8BB8BBBB888chl8BhBfd' --->  ["8BB8B8B88B",True]
8, '8' --->  ["",False]
1, 'j8BmB88B88gkBBlf8hg8888lbe88' --->  ["8BB88B",True]
0, '8j888aam' --->  ["",True]
"""


import re


some_string = input("Enter the string: ")
pairs = int(input("Enter the number of mating pairs : "))


list_pairs = re.findall(r'8B|B8', some_string)
bool_result = True if pairs <= len(list_pairs) else False
result = [''.join(list_pairs), bool_result]


print(result)
