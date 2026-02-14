# 1. Scrieti un regex care gaseste numele si varsta unei persoana din text:
# Exemplu text: Thomas S. (33), Eva M. ! (35), was last seen in Bucharest.
# Pattern gasit:
# Thomas S. (33)
# regex: [A-Z]{1}[a-z]+\s[A-Z]{1}\. \(\d+\)
#
# 2. Scrieti un regex care gaseste adresele de email.
# Exemple corecte: alex@email.com, alex123@gmail.com, ana.maria@yahoo.ro, mihai-ion@gmail.com, marcel@email123.com
# Exemple incorecte: alex!@email.com, name@yaho!o.com, ana@.com, ##@yahoo.com

# regex: [\w\.-]+@[\w]+\.[a-z]{2,}
