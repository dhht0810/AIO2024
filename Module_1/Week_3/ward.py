from abc import ABC, abstractmethod


class Ward:
    people = []

    def __init__(self, name):
        self.name = name

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward: {self.name}\n")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people.sort(key=lambda x: x.yob)

    def compute_average(self):
        count_teacher = 0
        total_yob = 0
        for person in self.people:
            if isinstance(person, Teacher):
                count_teacher += 1
                total_yob += person.yob
        return total_yob / count_teacher


class Person(ABC):
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name}, Yob: {self.yob}, Grade: {self.grade}" "\n")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name}, Yob: {self.yob}, Subject: {self.subject}" "\n")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name}, Yob: {self.yob}, Specialist: {self.specialist}" "\n")


# a
student1 = Student(name="studentA ", yob=2010, grade="7")
# student1.describe()

teacher1 = Teacher(name="teacherA ", yob=1969, subject="Math")
# teacher1.describe()

doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
# doctor1.describe()

# b
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
# ward1.describe()

# c
# print(ward1.count_doctor())

# d
ward1.sort_age()
# ward1.describe()

# e
print(ward1.compute_average())
