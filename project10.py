import csv


def load_students(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            students = []
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

            return students

    except FileNotFoundError:
        return []


def save_students(filename, students):
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "grade", "class"])

        writer.writeheader()

        for student in students:
            writer.writerow(student)


def add_student(students, name, grade, class_name):
    new_student = {
        "name": name,
        "grade": grade,
        "class": class_name}

    students.append(new_student)


def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student

    return None


def class_average(students, class_name):
    total = 0
    count = 0

    for student in students:
        if student["class"] == class_name:
            total = total + int(student["grade"])
            count = count + 1

    if count == 0:
        return 0

    return total / count


def top_student(students):
    if students == []:
        return None

    best_name = None
    best_grade = -1

    for student in students:
        grade = int(student["grade"])

        if grade > best_grade:
            best_grade = grade
            best_name = student["name"]

    return best_name


def print_all(students):
    if students == []:
        print("No students")

    else:
        for student in students:
            print("Name:", student["name"])
            print("Grade:", student["grade"])
            print("Class:", student["class"])
            print()


students = load_students("students.csv")

while True:
    print("1. Show all students")
    print("2. Add student")
    print("3. Find student")
    print("4. Class average")
    print("5. Top student")
    print("6. Save and exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print_all(students)

    elif choice == "2":
        name = input("Name: ")
        grade = input("Grade: ")
        class_name = input("Class: ")

        add_student(students, name, grade, class_name)
        save_students("students.csv", students)

        print("Student added")

    elif choice == "3":
        name = input("Student name: ")
        student = find_student(students, name)

        if student == None:
            print("Student not found")
        else:
            print(student)

    elif choice == "4":
        class_name = input("Class: ")
        average = class_average(students, class_name)

        print("Class average:", round(average, 2))

    elif choice == "5":
        student_name = top_student(students)

        if student_name == None:
            print("Not students")
        else:
            print("Top student:", student_name)

    elif choice == "6":
        save_students("students.csv", students)
        print("Students saved")
        break

    else:
        print("Invalid option")

    print()