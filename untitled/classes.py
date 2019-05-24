all_students = []


class Student:

    school = "NECC"

    def get_name(self):
        return self.name.capitalize() + " " + self.last_name.capitalize()

    def __init__(self, name: str, last_name: str = "N/A", st_id: int = -1):
        self.name = name
        self.id = st_id
        self.last_name = last_name
        all_students.append(self)

    def __str__(self):
        return "Student " + self.get_name()

    def get_school(self):
        return self.school


class HighSchoolStudent(Student):

    school = "Nuevo Liceo"

    def get_name(self):
        parent_value = super().get_name()
        return parent_value + " -High Schooler"
