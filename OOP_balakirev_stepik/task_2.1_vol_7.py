import re
import random
import string


class EmailValidator:
    def __new__(cls):
        return None

    @classmethod
    def check_email(cls, email):
        if EmailValidator.__is_email_str(email):
            if re.match(r'^[a-zA-Z0-9_]{1,100}@[a-zA-Z0-9-.]{1,50}$', email):
                return True
            else:
                return False

    @classmethod
    def get_random_email(cls):
        first_part = ''.join(
            [random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in
             range(0, random.randint(1, 101))])
        second_part = [random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for j in
                       range(5, random.randint(5, 51))]
        second_part.insert(random.randint(5, len(second_part) - 3), '.')
        return first_part + '@' + ''.join(second_part)

    @staticmethod
    def __is_email_str(email):
        if isinstance(email, str):
            return True


# ''''/
# ('/^((([0-9A-Za-z]{1}[-0-9A-z\.]{1,}[0-9A-Za-z]{1})|([0-9А-Яа-я]{1}[-0-9А-я\.]{1,}[0-9А-Яа-я]{1}))@([-A-Za-z]{1,}\.){1,2}[-A-Za-z]{2,})$/u', $item)
#
# ^( - параметр что маска начинается с начала текста
#     (
#         (  - этот блок отвечает за логин латиницей
#             [0-9A-Za-z]{1} - 1й символ только цифра или буква
#             [-0-9A-z\.]{1,} - в середине минимум один символ (буква, цифра, _, -, .) (не менее 1 символа)
#             [0-9A-Za-z]{1} - последний символ только цифра или буква
#         )
#         | - параметр "или/или" выбирает блок "латиница" или "кирилица"
#         (  - этот блок отвечает за логин кирилицей
#             [0-9А-Яа-я]{1} - 1й символ только цифра или буква
#             [-0-9А-я\.]{1,} - в середине минимум один символ (буква, цифра, _, -, .) (не менее 1 символа)
#             [0-9А-Яа-я]{1} - последний символ только цифра или буква
#         )
#     )
#     @ - обазятельное наличие значка разделяющего логин от домена
#     (
#         [-0-9A-Za-z]{1,} - блок может состоять из "-", цифр и букв (не менее 1 символа)
#         \. - наличие точки в конце блока
#     ){1,2} - допускается от 1 до 2 блоков по вышеукащанной маске (mail. , ru.mail.)
#     [-A-Za-z]{2,} - блок описывайющий домен вехнего уровня (ru, com, net, aero etc) (не менее 2 символов)
# )$ - параметр что маска заканчивается в конце текста
# /u - параметр позволяющий работать с кирилицей'''


# first_part = ''.join([random.choice(string.ascii_lowercase + string.digits) for i in range(0, random.randint(1, 101))])
# second_part = [random.choice(string.ascii_lowercase + string.digits) for j in range(5, random.randint(5, 51))]
# second_part.insert(random.randint(0, len(second_part) - 3), '.')
# print(first_part + '@' + ''.join(second_part))

print(EmailValidator.check_email("sc_lib@list_ru"))

'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HPgJtLb2NV8

Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае;
get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка).

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно. 
'''
