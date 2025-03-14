class Parent:
    def greet(self):
        print("Hello from the Parent class!")

class Child(Parent):
    def greet(self):
        super().greet()  
        print("Hello from the Child class!")


child_instance = Child()
child_instance.greet()
