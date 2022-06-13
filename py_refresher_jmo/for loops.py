# for loops

friends = ["Ryan","RyanC","Joanna","Tahna", "Jenn"]

for f in friends:
    print(f"{f} is my friend")



grades = [35,67,98,100,100]
total = 0

amount = len(grades)

for grade in grades:
    total += grade

avg = total/amount

print(f"The average grade is: {avg}")

theSum = sum(grades)

print(f"The sum of grades is {theSum}")


