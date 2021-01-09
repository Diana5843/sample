class Animal:
    age = 22

    def __init__(self, name):
        self.name = name

    def say(self, phrase):
        print(phrase)

    @staticmethod
    def print_type():
        print('Animal')


def get_name(self):
    return self.name


dog = Animal("Sharik")
spider = Animal(name="Garik")


print(dog.age)
print(spider.age)
print(Animal.age)

Animal.get_name = get_name