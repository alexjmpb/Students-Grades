from Student import Student, attribute_names


def classgpa(students_list):
    gpa_of_class = 0.0
    for i in range(len(students_list)):
        gpa_of_class += students_list[i].gpa
    return gpa_of_class / len(students_list)


def get_attributes(obj):
    attr_list = []
    for i in dir(obj):
        if not i.startswith("__"):
            attr_list.append(i)
    return list(reversed(attr_list))


def grades_array(add_grade=True):
    print("If you don't want to introduce more grades, type 'exit'")
    grade_list = []
    while add_grade:
        try:
            print(grade_list)
            grade = input("Introduce a grade: ")
            if grade == 'exit' and len(grade_list) > 0:
                add_grade = False
            elif grade == 'exit' and len(grade_list) == 0:
                print("You must introduce at least one grade")
            elif float(grade) >= 0:
                grade_list.append(float(grade))
        except ValueError:
            print("Introduce a valid input")
    return grade_list


def print_students(students_list):
    # iterate over students by index
    for student_selector in range(len(students_list)):
        # iterate over the attributes of each student
        for student_attr in get_attributes(students_list[student_selector]):
            if student_attr == get_attributes(students_list[student_selector])[-1]:
                print(f' {attribute_names[student_attr]}: {getattr(students_list[student_selector], student_attr)}')
            else:
                print(f' {attribute_names[student_attr]}: {getattr(students_list[student_selector], student_attr)}',
                      end=' |')
        if student_selector == len(students_list)-1:
            print(f'The GPA of the class is: {classgpa(students_list)}')


students = []
while True:
    try:
        choice = int(input("Introduce | 1: add student | 2: View Student list and GPA | 3: exit |: "))
        if choice == 1:
            students.append(Student(name=input("Introduce strudent's name: "), grade=grades_array()))
        elif choice == 2 and len(students) != 0:
            print_students(students)
        elif choice == 2 and len(students) == 0:
            print("You must add a student first")
        elif choice == 3:
            break
    except ValueError:
        print("introduce a valid input")