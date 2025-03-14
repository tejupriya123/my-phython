class Example:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        """A method that works with the class itself, not instances."""
        print(f"Class method called. Class variable: {cls.class_variable}")

    @staticmethod
    def static_method():
        """A method that doesn't depend on class or instance state."""
        print("Static method called. It doesn't access class or instance attributes.")



instance = Example("I am an instance variable")
Example.class_method()
instance.class_method()  
Example.static_method()
instance.static_method()  


print(f"Instance variable: {instance.instance_variable}")


print(f"Class variable (via instance): {instance.class_variable}")
print(f"Class variable (via class): {Example.class_variable}")


Example.class_variable = "Updated class variable"
Example.class_method()

print(f"Updated class variable (via instance): {instance.class_variable}")


Example.static_method()
