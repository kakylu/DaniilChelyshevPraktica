class Student:
    def __init__(self, first_name, last_name, birth_date, exams):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.exams = exams

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"


def load_students_from_file(file_path):
    group = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            data = line.split(",")

            first_name = data[0]
            last_name = data[1]
            birth_date = data[2]

            exams = []
            for i in range(3, len(data), 3):
                subject = data[i]
                exam_date = data[i + 1]
                teacher = data[i + 2]
                exams.append((subject, exam_date, teacher))

            student = Student(first_name, last_name, birth_date, exams)
            group.append(student)

    return group


def print_exam_table(group):
    print("Таблица предметов и дат экзаменов:")
    print("{:<15} {:<15} {:<15}".format("Предмет", "Дата экзамена", "Преподаватель"))
    print("-" * 45)

    for student in group:
        for exam in student.exams:
            subject, exam_date, teacher = exam
            print("{:<15} {:<15} {:<15}".format(subject, exam_date, teacher))

    print()


# Загрузка данных студентов из файла
file_path = "students.txt"
group = load_students_from_file(file_path)

# Вывод таблицы предметов и дат экзаменов
print_exam_table(group)
