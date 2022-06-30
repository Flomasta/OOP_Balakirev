const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Прописные буквы
const_lower_en = 'abcdefghijklmnopqrstuvwxyz'  # Строчные буквы


def decode_ceasar(string):
    res = ''
    for i in string:
        if not i.isalpha():
            res += i
        else:
            if i.isupper():
                const = const_upper_en
            elif i.islower():
                const = const_lower_en
            letter = const.find(i) + 17
            if letter > 26:
                letter = abs(letter - 26)
            res += (const[letter])
    return res


print(decode_ceasar("To be, or not to be, that is the question!"))
