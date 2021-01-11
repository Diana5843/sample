class Animals:
    age = 20
    gender = ""


class Vertebrates(Animals):

    def vertebrata_definition(self):
        print("Позвоночные — высший подтип хордовых. ")

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class WarmBlooded(Vertebrates):
    temp_warm = 40


class ColdBlooded(Vertebrates):
    temp_cold = 4


class Mamals(WarmBlooded):

    def feed_milk(self):
        print("Медедь - животное, отличительной особенностью которых является вскармливание детёнышей молоком")


class Bird(WarmBlooded):

    def fly(self):
        print("Ворона - теплокровное яйцекладущее позвоночное животное.")


class Fish(ColdBlooded):

    def swim(self):
        print("Лосось - парафилетическая группа водных позвоночных животных.")


class Reptiles(ColdBlooded):

    def crawl(self):
        print("Черепаха - традиционно выделяемый класс преимущественно наземных позвоночных животных из клады амниот")


class Amphibians(ColdBlooded):

    def mixed(self):
        print("Лягушка - занимает промежуточное положение между наземными и водными позвоночными животными")


bear = Mamals(name="Боря", gender="мужской пол")
crow = Bird(name="Клара", gender="женский пол")
salmon = Fish(name="Карла", gender="женский пол")
turtle = Reptiles(name="Мила", gender="женский пол")
toad = Amphibians(name="Крош", gender="мужской пол")


bear.feed_milk()
print('Имя:', bear.name, 'Возраст:', bear.age)
print(bear.gender, ',', bear.temp_warm, 'градусов температура тела',  '\n')

crow.fly()
print('Имя:', crow.name, 'Возраст:', crow.age)
print(crow.gender, ',', crow.temp_warm,  'градусов температура тела', '\n')

salmon.swim()
print('Имя:', salmon.name, 'Возраст:', salmon.age)
print(salmon.gender, ',', salmon.temp_cold, 'градуса температура тела', '\n')

turtle.crawl()
print('Имя:', turtle.name, 'Возраст:', turtle.age)
print(turtle.gender, ',', turtle.temp_cold, 'градуса температура тела', '\n')

toad.mixed()
print('Имя:', toad.name, 'Возраст:',  toad.age)
print(toad.gender, ',', toad.temp_cold, 'градуса температура тела', '\n')


