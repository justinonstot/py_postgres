#ClassMethodAndStaticMethod

## Related to "class methods and static methods"
## All functions inside a class that use the object as the first parameter are called "instance methods".
class ClassTest:
    def instance_method(self): #this is a method because it starts with "def" and has "self" as first parameter.
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls): ## this will be the class itself.
        print(f"Called the class_method of {cls}")


test = ClassTest()      ## "test" is an instance of the ClassTest class.
test.instance_method()