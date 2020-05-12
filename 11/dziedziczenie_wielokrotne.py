class UsefulStuff:
    def __init__(self, name):
        print(name, 'is used to make life easier!')

class Watch(UsefulStuff):
    def __init__ (self, w_name):
        self.w_name = w_name
        print(f"{self.w_name} shows time")
        super().__init__(self.w_name)

class Phone(UsefulStuff):
    def __init__(self, p_name):
        self.p_name = p_name
        print(f"{self.p_name} can call")
        super().__init__(self.p_name)

class SmartWatch(Watch, Phone):
    def __init__(self):
        print('Smartwatch is hot')
        super().__init__('SmartWatch')


