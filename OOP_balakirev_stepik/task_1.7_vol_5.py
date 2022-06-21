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
