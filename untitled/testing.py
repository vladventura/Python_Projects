all_students = []


def add(name: str, st_id: int = None):
    student = {"name": name, "id": st_id}
    all_students.append(student)


def get_students():
    students_format_name = []
    for student in all_students:
        students_format_name.append(student["name"].title())
    return students_format_name


def print_students():
    students_title = get_students()
    print(students_title)


def save(student):
    try:
        f = open("students.txt", "a")
        f.write(f"{student}\n")
        f.close()
    except Exception as e:
        print("Something went wrong!")
        print(e)


def load():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add(student)
        f.close()
    except Exception as e:
        print("It blew up bro")
        print(e)


load()
print_students()
response = True
while response:
    student_name = input("Enter the Student's name: ")
    student_id = input("Enter the Student's ID: ")
    add(student_name, student_id)
    save(student_name)
    answer = input("Would you like to add another Student into the database? Type (Y)es or (N)o: ")
    response = answer.lower() == "yes" or answer.lower() == "y"

