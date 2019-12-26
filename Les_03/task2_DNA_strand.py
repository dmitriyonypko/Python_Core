"""Task 2:
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells
and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other,
as "C" and "G". You have function with one side of the DNA (string, except for Haskell);
you need to get the other complementary side.
DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
"""


one_side_DNA = "AAAACCCGGT"


def DNA_strand(side_DNA):
    other_side_DNA =''
    for i in side_DNA:
        if i == 'A':
            other_side_DNA += i.replace('A', 'T')
            continue
        elif i == 'T':
            other_side_DNA += i.replace('T', 'A')
            continue
        elif i == 'C':
            other_side_DNA += i.replace('C', 'G')
            continue
        elif i == 'G':
            other_side_DNA += i.replace('G', 'C')
            continue
    return other_side_DNA

print(one_side_DNA)
print(DNA_strand(one_side_DNA))
