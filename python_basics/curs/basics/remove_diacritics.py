def remove(text):
    diacritics_dictionary = {
        "ă": "a",
        "â": "a",
        "î":"i",
        "ș": "s",
        "ț": "t",
    }
    keys = list(diacritics_dictionary.keys())
    for k in keys:
        diacritics_dictionary[k.upper()] = diacritics_dictionary[k].upper()
    print(diacritics_dictionary)

    for character in diacritics_dictionary:
        text = text.replace(character, diacritics_dictionary[character])
    return text

removed = remove("În România, Constituția din 1991, revizuită în 2003, stipulează în articolul 13 că „În România, limba oficială este limba română”")
print(removed)
