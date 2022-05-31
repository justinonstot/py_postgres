#ObjectOrientedProgramming1

## Make our life simpler; code that looks like real world models



# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

# def average(sequence):
#     return sum(sequence)/ len(sequence)


# print(average(student["grades"]))

# print(student.average()) # we have to create a student class

## Let's do the above, but in Object-Oriented way:

class Student:
     def __init__(self): # important and special we refer to ourselfs.
         self.name = "Rolf",
         self.age = 23

student = Student()  #runs the "init" method to create a new object. A funciton in a class is a method.

