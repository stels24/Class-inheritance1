class Car:

    def __init__(self):
        self.price = 1000000
    def horse_powers(self):
        return "350"



class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 1500000
    def horse_powers(self):
        return 300



class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 1200000
    def horse_powers(self):
        return 250


print(Car.horse_powers(1))
nissan = Nissan()
print(nissan.price)
print(nissan.horse_powers())
kia = Kia()
print(kia.price)
print(kia.horse_powers())
