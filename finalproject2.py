class Course:
    course_id_counter = 1
    courses_names = ["Language", "Design", "Programming", "Embroidery", "AI", "SEO"]
    course_levels = ["A", "B", "C"]

    def __init__(self, name, level):
        self.id = Course.course_id_counter
        Course.course_id_counter += 1
        self.name = name
        self.level = level

    def print_course_details(self):
        print(f"Course ID: {self.id}\nCourse Name: {self.name}\n"
              f"Course Level: {self.level}")


course1 = Course("Language", Course.course_levels)
course2 = Course("Design", Course.course_levels)
course3 = Course("Programming", Course.course_levels)
course4 = Course("Embroidery", Course.course_levels)
course5 = Course("AI", Course.course_levels)
course6 = Course("SEO", Course.course_levels)

courses_list = [course1, course2, course3, course4, course5, course6]

for course in courses_list:
    course.print_course_details()
    print("-" * 20)


class Student:
    student_id_counter = 1

    def __init__(self, name, level, courses):
        self.id = Student.student_id_counter
        Student.student_id_counter += 1
        self.name = name
        self.level = level
        self.courses = courses

    def print_student_details(self):
        print(f"Student ID: {self.id}\nStudent Name: {self.name}\n"
              f"Student Level: {self.level}\nStudent Courses: {self.courses}")

    def add_new_course(self, course_name):
        self.courses = student_courses.append(course_name)


s1 = Student("Samah", "A", ["Language"])
s2 = Student("Maha", "B", ["AI", "Language"])
s3 = Student("Rasha", "C", ["Programming", "SEO"])
s4 = Student("Doha", "A", ["Embroidery"])
s5 = Student("Dalal", "B", ["Design", "Embroidery"])

# method to display student_details
students = [s1, s2, s3, s4, s5]
for student in students:
    student.print_student_details()
    print("-" * 20)

course_levels = ["A", "B", "C"]
student_levels = ["A", "B", "C"]
courses_names = ["Language", "Design", "Programming", "Embroidery", "AI", "SEO"]
student_courses = ["Language", "AI", "SEO"]

# method to add new course to student courses done by the programmer itself

course_level = input("Select course level (A, B , C): ").capitalize()
if course_level in course_levels:
    student_level = input("Enter your level (A, B , C): ").capitalize()
    if course_level == student_level:
        Student.add_new_course(s1, "English")
        print("Course added successfully,", s1.name, "courses are: ", student_courses)
    else:
        print("Course can not be added.")
else:
    print("Select level again.")

print("-" * 20)

# method to add new course to student courses by asking the user

new_course = input("Enter course name: ").capitalize()
if new_course in courses_names:
    course_level = input("Select course level (A, B , C): ").capitalize()
    if course_level in course_levels:
        student_level = input("Enter your level (A, B , C): ").capitalize()
        if course_level == student_level:
            student_courses.append(new_course)
            print("Your courses are: ", student_courses)
        else:
            print("Course can not be added.")
    else:
        print("Select level again.")
else:
    print("Course not exist.")

print("-" * 20)

studentsID = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# 1. Add new student
def add_student():
    student_name = input("Enter student name: ")
    student_level = input("Select level (A, B , C): ").capitalize()
    student_levels = ["A", "B", "C"]
    if student_level in student_levels:
        print("Student saved successfully.")
    else:
        print("Select level again.")


# 2. Remove student:
def remove_student():
    student_id = int(input("Enter student ID: "))
    if student_id in studentsID:
        studentsID.pop(student_id - 1)
        print("Delete done successfully")
        print(studentsID)
    else:
        print("User not exist.")

# 3. Edit Student


def edit_student():
    student_id = int(input("Enter student ID: "))
    if student_id in studentsID:
        new_name = input("Enter new name: ")
        student_level = input("Select new level (A, B , C): ").capitalize()
        student_levels = ["A", "B", "C"]
        if student_level in student_levels:
            print("Student edited successfully.")
        else:
            print("Select level again.")
    else:
        print("User not exist.")

# 4. Display all students


def display_students():
    for student in students:
        student.print_student_details()
        print("*" * 20)


# 5. Create new course:
def new_course():
    class_name = input("Enter class name: ")
    course_level = input("Select course level (A, B , C): ").capitalize()
    course_levels = ["A", "B", "C"]
    if course_level in course_levels:
        print("New course saved successfully.")
    else:
        print("Level not exist.")


# 6 . Add Course to student
def add_course():
    student_id = int(input("Enter student id: "))
    if student_id in studentsID:
        courses_names = ["Language", "Design", "Programming", "Embroidery", "AI", "SEO"]
        student_course_list = ["Language", "AI", "SEO"]
        course_name = input("Enter course Name: ").capitalize()
        if course_name in courses_names:
            student_course_list.append(course_name)
            print("Your courses are: ", student_course_list)
        else:
            print("Course not exist.")
    else:
        print("User not exist.")

# 0. Leave


def exit():
    print("See you later.")


def menu():
    select = 0
    while select != 5:
        print("1. Add New Student")
        print("2. Remove Student")
        print("3. Edit Student")
        print("4. Display All Students")
        print("5. Create New Course")
        print("6. Add Course To Student")
        print("0. Exit")


print("Welcome students")
print("Choose one of the options")
print("----------------------------")
print("1. Add New Student")
print("2. Remove Student")
print("3. Edit Student")
print("4. Display All Students")
print("5. Create New Course")
print("6. Add Course To Student")
print("0. Exit")
print("----------------------------")
select = int(input("Choose an option: "))
if select == 1:
    add_student()
if select == 2:
    remove_student()
if select == 3:
    edit_student()
if select == 4:
    display_students()
if select == 5:
    new_course()
if select == 6:
    add_course()
if select == 0:
    exit()
