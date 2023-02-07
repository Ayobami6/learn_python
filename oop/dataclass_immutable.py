# 3.7 feature data class
from dataclasses import dataclass, field


@dataclass(frozen=True)  # making the class attribute immutable
class Student:
    name: str = "Ayo"
    cohort: int = field(default=None)
    specialization: str = None
    # this is a private instance attribute
    # __password: str


student1 = Student()

#  Will give frozen instance error
# student1.name = "Wisdom"

print(student1.name)
