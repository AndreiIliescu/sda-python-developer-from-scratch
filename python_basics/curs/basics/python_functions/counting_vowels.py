def find_vowels(text):
    vowel = {}
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']

    for letter in text:
        if letter in vowel_list:
            vowel[letter] = vowel.get(letter, 0) + 1

    return vowel

if __name__ == '__main__':
    text_input = input('Set a text: ').lower()
    print(find_vowels(text_input))
