const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Прописные буквы
const_lower_en = 'abcdefghijklmnopqrstuvwxyz'  # Строчные буквы


def decode_ceasar(string):
    lst = []
    for j in range(26):

        res = ''
        for i in string:
            if not i.isalpha():
                res += i
            else:
                if i.isupper():
                    const = const_upper_en
                elif i.islower():
                    const = const_lower_en
                letter = const.find(i) - j
                if letter > 26:
                    letter = abs(letter - 26)
                res += (const[letter])
        lst.append(res)
    return lst


print(decode_ceasar("Hawnj pk swhg xabkna ukq nqj."))
