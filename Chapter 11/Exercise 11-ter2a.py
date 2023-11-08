# Source: https://www.geeksforgeeks.org/multiple-inheritance-in-python/
# Python Program to depict multiple inheritance
# when every class defines the same method

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    def m(self):
        # Method Resolution Order (MRO): The parent classes are searched in a left-right fashion and each class is
        # searched once.
        super().m()
        # Directly calling Class 3 method
        # Class3.m(self)
        print("In Class4")


obj = Class4()
obj.m()

Class2.m(obj)
Class3.m(obj)
Class1.m(obj)
