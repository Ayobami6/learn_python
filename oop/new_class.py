from typing import Optional

# Base class


class AlxSchool:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization


class Student(AlxSchool):

    SPECIALIZATION = ["Backend", "Frontend"]

    @classmethod
    def getspecs(cls):
        return cls.SPECIALIZATION

    @classmethod
    def change_spec(cls, new):
        cls.SPECIALIZATION = new
        return cls.SPECIALIZATION

    @classmethod
    def add_spec(cls, new):
        cls.SPECIALIZATION.append(new)
        return cls.SPECIALIZATION

    def __init__(self, name, specialization, cohort) -> None:

        super().__init__(name, specialization)

        self.cohort = cohort
        # self.specialization = specialization
        self.__password = "My password"
        # if specialization not in Student.SPECIALIZATION:
        #     print("Adding a new spec")
        #     self.add_spec(specialization)
        # # raise ValueError(f"{specialization} is not found")

    def getname(self):
        return self.name

    def get_password(self):
        return self.__password

    def changecohort(self, new_cohort):
        self._Student__newcohort = new_cohort

    def get_cohort(self):
        if hasattr(self, "_Student__newcohort"):
            return self._Student__newcohort
        else:
            return self.cohort

    def get_spec(self):
        return self.SPECIALIZATION

    def changespec(self, new):
        self.SPECIALIZATION = new
        return self.SPECIALIZATION

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
        return self.__password

    def __str__(self):
        return f"My name is {self.name}, I'm in cohort {self.cohort}"

    def __getattribute__(self, name):
        if name == "password":
            password = super().__getattribute__("_Student__password")
            return password
        return super().__getattribute__(name)


student1 = Student("Wale", "Backend", 10)
print(getattr(student1,  "password", None))

print(student1)
# print(repr(student1))
print(student1.specialization)


# print(Student.__mro__)
# student2 = Student("Mallo", "Backend", 9)

# student3 = Student("Mallo", "Full Satck", 9)

# student3.add_spec("Full Stack")


# print(student1.password)
# student1.password = "This is new"
# print(student1.password)

# print(Student.SPECIALIZATION)

# student1.change_spec(("new", "new"))

# print(Student.SPECIALIZATION)

# student1.changespec(("old", "old"))

# print(Student.SPECIALIZATION)
