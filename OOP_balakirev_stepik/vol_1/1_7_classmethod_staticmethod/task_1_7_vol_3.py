import re


class CardCheck:
    @staticmethod
    def check_card_number(number):
        return True if re.match(r'\d{4}-\d{4}-\d{4}-\d{4}', number) else False

    @staticmethod
    def check_name(name):
        return True if re.match(r'^[A-Z]+\s[A-Z]+$', name) else False
