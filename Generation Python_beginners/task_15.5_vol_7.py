const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Прописные буквы
const_lower_en = 'abcdefghijklmnopqrstuvwxyz'  # Строчные буквы


def decode_ceasar(string):
    separated_string = string.split()
    res = ''
    for i in separated_string:
        shit = [1 for j in i if j.isalpha()]
        for j in i:
            if not j.isalpha():
                res += j
            else:
                if j.isupper():
                    const = const_upper_en
                elif j.islower():
                    const = const_lower_en
                letter = const.find(j) + sum(shit)
                if letter >= 26:
                    letter = abs(letter - 26)
                res += (const[letter])
        res += ' '

    return res


print(decode_ceasar(input()))
