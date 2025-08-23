# define a dictionary with student marks
student_marks = {"Alice" : "85", "Mark" : "97", "Mike" : "81", "Smith" : "81"}
print(student_marks)

# Get student name as input
input_1 = input("Enter the student's name : ")

# Validate and print marks
if input_1 in student_marks:
    student_mark = student_marks[input_1]
    print(f"{input_1}'s marks : ",student_mark)
else:
    print("Student not found.")