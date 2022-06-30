TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(DialogWindows) if TYPE_OS == 1 else super().__new__(DialogLinux)
        setattr(instance, 'name', args[0])
        return instance

    def __init__(self, name):
        self.name = name


dg = Dialog(1234)
print(type(dg))
print(dg.name)
print(dg.__dict__)
print(DialogWindows.__dict__)
