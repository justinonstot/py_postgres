#destructuringVariables

# x = (5,11) # a tuple. Brackets are not "necessary" though except to unconfuse 

# y = 5,11

# print(type(x)) #both x and y show as type of "tuple"
# print(type(y))

# t = 5,11
# a,b = t

# print(a)
# print(b)

student_attendance = {"Rolf":96, "Bob":80, "Anne":100}

print(list(student_attendance.items())) # a list of tuples

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


people = [("Bob", 42, "Mechanic"),("James", 24, "Artist"),("Harry", 32, "Lecturer")]

for name, age, profession in people:
        print(name, age, profession)

person = ("Bob", 42, "Mechanic")

name, _, profession = person

print(name, profession)

[1,2,3,4,5]

head, *tail = [1,2,3,4,5] # split in two. the "1" becomes "head", and all other values go in tail

print(type(head), type(tail))