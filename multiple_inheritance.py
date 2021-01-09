class Auto:
    def ride(self):
        print("Автомобиль едет по дороге")


class Boat:
    def swim(self):
        print("Лодка плывет в океане")

class Amphibiah(Auto, Boat):
    pass

a = Amphibiah()
a.ride()
a.swim()