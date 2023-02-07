# 3.7 feature data class
from dataclasses import dataclass

# The dataclass decorator will automatically re-write the class
# to add the init function


@dataclass
class Student:
    name: str
    cohort: int
    specialization: str
    # this is a private instance attribute
    # __password: str

    def __post_init__(self):
        self.__password = "This is my password"

    @property  # password getter
    def get_password(self):
        return self.__password

    # We use it to set value to our private intsance attribute
    # So when we assign value to it we won't get attribute error
    @get_password.setter  # password setter
    def password(self, password):
        self.__password = password
        return self.__password

    def getname(self) -> str:
        return self.name


student1 = Student("Ayobami", 10, "Backend")
student2 = Student("Bunmi", 10, "Backend")
student3 = Student("Ayobami", 10, "Backend")

print(student1.name)
print(student2.name)

print(student1.get_password)

#  dataclass automatically implemet it __repr__ function and __eq__
print(student1)

# __eq__

print(student1 == student3)
