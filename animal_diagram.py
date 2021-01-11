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

bear_paws = 4
bear_teeth = 40

bear.feed_milk()

print('Имя:', bear.name, 'Возраст:', bear.age)
print(bear.gender, ',', bear.temp_warm, 'градусов температура тела')
print('Количество лап:', bear_paws, '\n', 'Количество зубов: ', bear_teeth, '\n')

crow.paws = 2
crow.eat = "Всеядны и питаются абсолютно всем, что, по их мнению, окажется съедобным."

crow.fly()

print('Имя: ', crow.name, 'Возраст: ', crow.age)
print(crow.gender, ',', crow.temp_warm,  'градусов температура тела')
print('Количество лап: ', crow.paws, '\n', crow.eat, '\n')

salmon.eat = "Лосось питается в основном мелкой рыбой, килькой и салакой."
salmon.caviar = "Самка тихоокеанского лосося во время нереста откладывает от 1500 до 7000 икринок."

salmon.swim()

print('Имя:', salmon.name, 'Возраст:', salmon.age)
print(salmon.gender, ',', salmon.temp_cold, 'градуса температура тела')
print(salmon.eat, '\n', salmon.caviar, '\n')

turtle.lifespan = "Черепахи вполне могут дожить и до 200 лет, если будут находиться в благоприятных для них условиях."

turtle.crawl()

print('Имя:', turtle.name, 'Возраст:', turtle.age)
print(turtle.gender, ',', turtle.temp_cold, 'градуса температура тела')
print(turtle.lifespan)

toad.eat = "Лягушки, питается различными насекомыми: личинками стрекоз, водяными жуками и их личинками, моллюсками. "

toad.mixed()

print('Имя:', toad.name, 'Возраст:',  toad.age)
print(toad.gender, ',', toad.temp_cold, 'градуса температура тела')
print(toad.eat)


