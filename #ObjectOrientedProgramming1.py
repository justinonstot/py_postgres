#ObjectOrientedProgramming1

## Make our life simpler; code that looks like real world models



# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

# def average(sequence):
#     return sum(sequence)/ len(sequence)


# print(average(student["grades"]))

# print(student.average()) # we have to create a student class

## Let's do the above, but in Object-Oriented way:

class Student:
    ## the __init__ method is always called first.
    def __init__(self, name, grades): # important and special we refer to ourselfs.
         self.name = name
         self.grades = grades 
    
    def average_grade(self): # init method runs and you get a new object. When you call 
        return sum(self.grades) / len(self.grades)  

student = Student("Bob", [80, 92, 76, 56, 100])  #runs the "init" method to create a new object. A funciton in a class is a method.
print(student.name)
print(student.average_grade())