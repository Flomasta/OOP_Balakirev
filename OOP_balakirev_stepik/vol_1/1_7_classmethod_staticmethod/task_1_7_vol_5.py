class AppStore:
    def __init__(self):
        self.applications = []

    def add_application(self, app):
        ''' добавление нового приложения app в магазин'''
        self.applications.append(app)

    def remove_application(self, app):
        '''удаление приложения app из магазина'''
        self.applications.remove(app)

    def block_application(self, app):
        '''блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True)'''
        app.blocked = True

    def total_apps(self):
        '''возвращает общее число приложений в магазине'''
        return len(self.applications)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
# store.remove_application(app_youtube)

print(app_youtube)
print(store.applications[store.applications.index(app_youtube)])


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Y4Hvpg4FuKs
#
# Подвиг 10 (на повторение). Объявите класс AppStore - интернет-магазин приложений для устройств под iOS. В этом классе должны быть реализованы следующие методы:
#
# add_application(self, app) - добавление нового приложения app в магазин;
# remove_application(self, app) - удаление приложения app из магазина;
# block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
# total_apps(self) - возвращает общее число приложений в магазине.
#
# Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):
#
# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)
# Здесь Application - класс, описывающий добавляемое приложение с указанным именем. Каждый объект класса Application должен содержать локальные свойства:
#
# name - наименование приложения (строка);
# blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).
#
# Как хранить список приложений в объектах класса AppStore решите сами.
#
# P.S. В программе нужно только объявить классы с указанным функционалом.
