class Animal:
    name = "Животное"
    age = 22

    def __init__(self, name):
        self.name = name

    def say(self, phrase):
        print(phrase)


dog = Animal("Sharik")
spider = Animal(name="Garik")

# print(dog.name)
# print(spider.name)
# print(Animal.name)

