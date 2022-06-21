class Viber:
    messages = []

    @classmethod
    def add_message(cls, msg):
        '''добавление нового сообщения в список сообщений'''
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        '''удаление сообщения из списка'''
        cls.messages.remove(msg)

    @classmethod
    def set_like(cls, msg):
        '''поставить/убрать лайк для сообщения msg (если лайка нет то он ставится, если уже есть, то убирается)'''
        msg.fl_like = True

    @classmethod
    def show_last_message(cls, n):
        '''отображение последних сообщений'''
        return cls.messages[:n:]

    @classmethod
    def total_messages(cls):
        '''возвращает общее число сообщений'''
        return len(cls.messages)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
print(Viber.total_messages())
print(Viber.messages[0].text)
