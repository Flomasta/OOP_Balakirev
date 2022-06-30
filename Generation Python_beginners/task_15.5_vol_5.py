const_upper_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
const_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'


def decode_ceasar(string):
    res = ''
    for i in string:
        if not i.isalpha():
            res += i
        else:
            if i.isupper():
                const = const_upper_ru
            elif i.islower():
                const = const_lower_ru
            letter = const.find(i) - 7
            if letter > 32:
                letter = abs(letter - 32)
            res += (const[letter])
    return res


print(decode_ceasar("Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг"))
