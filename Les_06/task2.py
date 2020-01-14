"""Task 2:
Next Version
You're fed up about changing the version of your software manually.
Instead, you will create a little script that will make it for you.
Exercice
Create a function nextVersion, that will take a string in parameter,
and will return a string containing the next version number.
For example:
nextVersion("1.2.3") === "1.2.4";
nextVersion("0.9.9") === "1.0.0";
nextVersion("1") === "2";
nextVersion("1.2.3.4.5.6.7.8") === "1.2.3.4.5.6.7.9";
nextVersion("9.9") === "10.0";
Rules
All numbers, except the first one, must be lower than 10:
if there are, you have to set them to 0 and increment the next number in sequence.
"""


version = input('Enter version number: ')


def next_version(version):
    """Return a string containing the next version number."""
    list_version = list(map(int, version.split('.')))
    slicE = len(str(list_version[0]))

    version = version.replace('.', '')
    next_version = str(int(version) + 1)

    if len(version) < len(next_version): 
        result = next_version[:slicE] + '.'.join(next_version[slicE:])
    elif list_version[0] > 9 and len(version) == len(next_version):
        slicE -= 1
        result = next_version[:slicE] + '.'.join(next_version[slicE:])
    else:
        result = '.'.join(next_version)
    return 'Next version: ' + result


print(next_version(version))
