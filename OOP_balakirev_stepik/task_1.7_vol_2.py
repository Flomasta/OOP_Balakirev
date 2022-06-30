from string import ascii_lowercase, digits
import re


# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return f'<p class=\'login\'>{self.name}: <input type=\'text\' size={self.size} />'

    @classmethod
    def check_name(cls, name):
        if re.match('^[a-zA-zА-Яа-яЁё0-9_\s]{3,50}$', name):
            return True
        else:
            raise ValueError('некорректное имя поля')


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size

    def get_html(self):
        return f'<p class=\'password\'>{self.name}: <input type=\'text\' size={self.size} />'

    @classmethod
    def check_name(cls, name):
        if not re.match('^[a-zA-zА-Яа-яЁё0-9_\s]{3,50}$', name):
            raise ValueError('некорректное имя поля')
        else:
            return True


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

login_1 = FormLogin(TextInput("(((Логин"), PasswordInput("Пароль"))
