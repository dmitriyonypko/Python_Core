"""Task 4:

For a given chemical formula represented by a string,
count the number of atoms of each element contained in the molecule
and return an object.

For example:
var water = 'H2O';
parseMolecule(water); // return {H: 2, O: 1}

var magnesiumHydroxide = 'Mg(OH)2';
parseMolecule(magnesiumHydroxide); // return {Mg: 1, O: 2, H: 2}

var fremySalt = 'K4[ON(SO3)2]2';
parseMolecule(fremySalt); // return {K: 4, O: 14, N: 2, S: 4}

As you can see, some formulas have brackets in them.
The index outside the brackets tells you that you have to multiply
count of each atom inside the bracket on this index.
For example, in Fe(NO3)2 you have one iron atom,
two nitrogen atoms and six oxygen atoms.

Note that brackets may be round,
square or curly and can also be nested.
Index after the braces is optional.
"""

# input: s = 'K4[ON(SO3)2]2{H2O}3Mg5'
# output: dict = {K: 4, O: 17, N: 2, S: 4, H: 6, Mg: 5}

chemical_formula = 'K4[ON(SO3)2]2{H2O}3Mg5'


def parseMolecule(chemical_formula):
    """Count the number of atoms of each element contained in the molecule
    and return an object."""
    
    dict_brackets = {'}': '{', ']': '[', ')': '('}
    
    # Соединяем атомы у которых 2 буквы в названии
    helper_list = list(chemical_formula)
    for index, item in enumerate(helper_list):
        if item.islower():
            helper_list[index-1] = helper_list[index-1] + item
            del helper_list[index]
    
    helper_list.reverse()
    
    # Заносим все атомы в словарь
    dict_atoms = {item: 0 for item in helper_list if item.isalpha()}
    
    # Раскрываем скобки
    i = 0
    while i < len(helper_list):
        num = 1
        if helper_list[i].isdigit():
            num = int(helper_list[i])
            j = i + 1
            if helper_list[j] in dict_brackets:
                value = dict_brackets[helper_list[j]]
                while helper_list[j] != value:
                    if helper_list[j].isalpha():
                        helper_list[j] *=  num
                    j += 1
                else:
                    del helper_list[i]
        i += 1
    
    # Умножаем цифру которая стоит перед атомом на атом
    i = 0
    while i < len(helper_list):
        num = 1
        if helper_list[i].isdigit():
            num = int(helper_list[i])
            j = i + 1
            helper_list[j] *= num
            del helper_list[i]
        i += 1

    for atom in dict_atoms:
        dict_atoms[atom] = ''.join(helper_list).count(atom)
    
    return dict_atoms


print(parseMolecule(chemical_formula))
