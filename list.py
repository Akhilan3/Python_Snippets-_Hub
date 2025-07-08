# MINI STUDENT REPORT SYSTEM USING LIST METHODS
# CREATING A LIST 

students = ["Avain","Max","Herod","Oleg","Jenny"]
print(students)

# ADDING FEW MORE STUDENTS TO THE LIST
additional_students = ["Keny","Ram","Abigail"]
students.append(additional_students)
print(students)

# TOTAL NUMBER OF STUDENTS
print("The total number of students in the list is",len(students))

# REMOVING TOTAL LIST
students.clear()
additional_students.clear()
print("Student lists are cleared.")