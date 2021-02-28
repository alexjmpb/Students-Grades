def gpa_value(grades):
    avg = 0
    for i in grades:
        avg += i
    avg = avg / len(grades)
    return avg


def is_passing_check(gpa):
    if gpa >= 10:
        return True
    else:
        return False


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.gpa = gpa_value(grade)
        self.is_passing = is_passing_check(gpa_value(grade))


attribute_names = {
    "name": "Name",
    "note1": "Note 1",
    "note2": "Note 2",
    "grade": "Grade",
    "gpa": "GPA",
    "is_passing": "Is passing?",
    True: "Yes"
}

