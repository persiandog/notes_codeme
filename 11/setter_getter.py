class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__serial_number = 'XFHTHRU98865'

    def get_serial_number(self):
        return self.__serial_number

    def set_serial_number(self, nr):
        self.__serial_number = nr

    def __str__(self):
        return f"Laptop {self.brand} | {self.model} | #{self.__serial_number}"


comp = Laptop('Asus', '+++')

print(comp.get_serial_number())
print(comp)

print('-----------------------')
comp.set_serial_number('AUJFHGGJ')
print(comp)