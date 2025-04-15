#Manage Student Data Using Tuples and Various Methods
def create_students():
    return [
        ("Alice", 1, (85, 90, 78), "B"),
        ("Bob", 2, (75, 88, 92), "A"),
        ("Charlie", 3, (60, 65, 70), "C")
    ]

def display_students(students):
    if not students:
        print("No student records available.")
    else:
        for s in students:
            print(s)


def add_student(students, name, roll, marks, grade):
    student = (name, roll, marks, grade)
    students.append(student)
    print("Student added.")
    return students

def search_student(students, roll):
    for s in students:
        if s[1] == roll:
            print("Student found:", s)
            return s
    print("Student not found.")
    return None


def show_total_marks(students):
    for s in students:
        total = sum(s[2])
        print(f"{s[0]} (Roll {s[1]}) - Total Marks: {total}")


def update_grade(students, roll, new_grade):
    for i in range(len(students)):
        if students[i][1] == roll:
            name, r, marks, _ = students[i]
            students[i] = (name, r, marks, new_grade)
            print("Grade updated.")
            break
    else:
        print("Student not found.")
    return students


def remove_student(students, roll):
    for i in range(len(students)):
        if students[i][1] == roll:
            del students[i]
            print("Student removed.")
            break
    else:
        print("Student not found.")
    return students


def main():
    students = create_students()
    
    print("Initial Students:")
    display_students(students)

    students = add_student(students, "Diana", 4, (90, 85, 88), "A")
    
    search_student(students, 2)

    print("\nTotal Marks:")
    show_total_marks(students)

    students = update_grade(students, 3, "B")
    students = remove_student(students, 1)

    print("\nFinal List:")
    display_students(students)

main()
