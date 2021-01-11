class Mecanical:
    def swim(self):
        print("Механизм плывет в океане")

class Auto:
    def swim(self):
        print("Автомобиль плывет в океане")


class Boat:
    def swim(self):
        print("Лодка плывет в океане")


class Amphibiah(Auto, Boat):
    pass


a = Amphibiah()
a.swim()

# print(isinstance(a, Amphibiah))
# print(isinstance(a, Auto))
# print(isinstance(a, Boat))

