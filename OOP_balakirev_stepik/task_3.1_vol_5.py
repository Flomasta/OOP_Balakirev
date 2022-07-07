class SmartPhone:

    def __init__(self, model):
        self.apps = []
        self.model = model

    def add_app(self, app):
        if not any([type(i) == type(app) for i in self.apps]):
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self, name='ВКонтакте'):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max=1024):
        self.name = 'YouTube'
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list, name='Phone', ):
        self.name = name
        self.phone_list = phone_list


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
