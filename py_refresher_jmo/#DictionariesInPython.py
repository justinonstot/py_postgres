#DictionariesInPython

friend_ages = {"Rolf": 24,"Bob":48, "Anne": 56}
student_attendance = {"Rolf": 96,"Bob":80, "Anne": 100}
search = 'Jim'

# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}%")

# better  way, using a variable for each key and value
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}%")


# is a value a key
if search in student_attendance:
    print(f"{search} attended {student_attendance[search]} %" )
else:
    print(f"{search} is not in this class")

attendance_values = student_attendance.values()

print("the average attendance is: ", sum(attendance_values)/len(attendance_values), "%")

# for keys in friend_ages:
#     print(value)

# friends = [
#     {"name":"Rolf","age":24},
#     {"name":"Jenn","age":48},
#     {"name":"Bill","age":56}
# ]

# print(friends[0])
# print(friends[0]["name"])