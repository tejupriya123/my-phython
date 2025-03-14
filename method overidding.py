class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")


animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

cat = Cat()
cat.speak()
