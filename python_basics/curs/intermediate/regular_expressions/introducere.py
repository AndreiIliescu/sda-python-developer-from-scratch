### Regular expressions ###

# When using regular expressions, we must remember that some characters have a special meaning. Those are:

#     dot: . – any character except a newline character. The pattern .la matches the strings: “Ola”, “ala” and ” Ela”,
#     question mark: ? – matches zero or one occurrence of the preceding character. The pattern Olk?a matches “Ola” and “Olka”,
#     plus: + – means one or more occurrences. The pattern a+le matches the strings: “ale”, “aaale”, “aaaaale”, etc.,
#     asterisk: * – stands for any number of occurrences of a character (including zero). The pattern a*la matches the strings: “la”, “ala”, “aaaaala”, etc.,
#     square brackets match any of the characters they contain. The pattern [OA]la matches “Ola” and “Ala”. We can also specify a range of characters by using a hyphen. The pattern [a-z]al matches the word starting with any lowercase letter followed by a string “al”, i.e. “mal”, “pal” or “eal”,
#     parentheses allow you to group characters in an expression so that you can collectively apply different modifiers to them,
#     the braces provide the number of repeats. The pattern a(la){1,3} matches all strings starting with “a” followed by one to three strings “la”, tj. “ala”, “alala” and “alalala”,
#     caret: ^ – negation of the characters given in square brackets. That is, to the pattern [^OA]la matches “Ela” i “Bla”, but “Ola” and not “Ala”,
#     pipeline: | stands for an alternative, e.g. to a pattern Alice has (dog|cat) both the string “Ala has a cat” and “Ala has a dog” will match,
#     caret ^ at the beginning of a pattern means to match the beginning of a line. The pattern ^ [a-z]* will not match e.g. “Barbara has a hedgehog”, because the string does not start with a lowercase letter,
#     Likewise, the dollar sign __ $ __ matches the end of a line.

# [A-Z] toate literele mari
# [A-Za-z] toate literele mari si mici
# [0-9]
# \d echivalent cu a scrie [0-9]
# \w echivalent cu [A-Za-z0-9]
# \s reprezinta un spatiu

import re

# search() cauta un pattern intr-un text
# daca exista va returna Match la primul gasit
result = re.search(r"[A-Z]la", "ala Ola Ela")
print(result)

# match() verifica doar inceputul textului
result = re.match(r"[A-Z]la", "ala Ola ela")
print(result)

# fullmatch() verifica daca intregul text se potriveste cu pattern-ul
result = re.fullmatch(r"[A-Z]la", "Ela")
print(result)

# findall() va returna o lista cu toate match-urile dupa pattern
result = re.findall(r"[A-Z]la", "ala ola Ela Elaa, !! Zla 128")
print(result)

# finditer(), la fel ca findall(), dar returneaza un iterator
result = re.finditer(r"[A-Z]la", "ala ola Ela Elaa, !! Zla 128")
for elem in result:
    print(elem)

# split() va imparti textul dupa un pattern
fruits = "apple  ,, banana;;;;;!!! lemon    :::::;;;;!! orange"
result = re.split(r"[,\s;!:]+", fruits)
print(result)

# sub() va inlocui cuvinte din textul original dupa un pattern
result = re.sub(r"[a-z]{3}", "dog", "Alice has a cat.")
print(result)

# subn() asemanator cu sub(), dar ne va returna si numarul de substitutii facute
result = re.subn(r"[a-z]{3}", "dog", "Alice has a cat.")
print(result)

# Exemplu cu |
# Are rolul unui sau
# test123exemplu45778  hello1990
# output: ['test', '123', 'exemplu', '45778', 'hello', '1990']
result = re.findall(r"\d+|[a-zA-Z]+", "test123exemplu45778  hello1990")
print(result)
