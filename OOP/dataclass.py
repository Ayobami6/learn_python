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

    def getname(self) -> str:
        return self.name


student1 = Student("Ayobami", 10, "Backend")
student2 = Student("Bunmi", 10, "Backend")
student3 = Student("Ayobami", 10, "Backend")

print(student1.name)
print(student2.name)

#  dataclass automatically implemet it __repr__ function and __eq__
print(student1)

# __eq__

print(student1 == student3)
