class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


def make_animal_speak(animal):
    print(animal.speak())



animals = [Dog(), Cat()]

for animal in animals:
    make_animal_speak(animal)
