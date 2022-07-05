class PhoneBook:
    def __init__(self):
        self.phone_book = []

    def add_phone(self, phone):
        self.phone_book.append(phone)

    def remove_phone(self, indx):
        if 0 <= indx < len(self.phone_book):
            del self.phone_book[indx]

    def get_phone_list(self):
        return self.phone_book


class PhoneNumber:
    def __init__(self, number, fio):
        if self.check_phone(number):
            self.number = number
        if self.check_fio(fio):
            self.fio = fio

    @classmethod
    def check_phone(cls, data):
        if len(str(data)) == 11 and str(data).isalnum():
            return True

    @classmethod
    def check_fio(cls, fio):
        if isinstance(fio, str):
            return True


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
for i in phones:
    print(i.fio)
