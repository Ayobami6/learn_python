# Abstract base class
# A template for other subclass to inherit from
# Reasons while you want to use Abstract base class
# 1. You don't want user to use or instantiate the base class cause its a blueprint
# 2. To have a constraint that subclassess must implement

# Importing the Abstact base class ABC from abc
from abc import ABC, abstractmethod
from typing import Optional


class AlxSchool(ABC):  # inheriting from the Abstract base class
    def __init__(self, name: str, specialization: str) -> None:
        super().__init__()
        self.name = name
        self.specialization = specialization

    @abstractmethod  # This tells python that there is no implementation in the
    # base class and all subclass has to overwrite this method
    def enrol(self) -> None:
        pass

    @abstractmethod
    def defer(self) -> None:
        pass


class Student(AlxSchool):
    STUDENT = False

    # initialize function

    def __init__(self, name: Optional[str] = None, specialization: Optional[str] = None, cohort: Optional[int] = None) -> None:
        """ instance initialization function

        Args:
            name (str): name of student
            cohort (int): student cohort

        Returns:
                None
        """
        # Calling the super class init funtion to access base class instance
        # attributes
        if Student.STUDENT is True:
            super().__init__(name, specialization)  # You don't need to parse self
            self.cohort = cohort

    # Overwriting the enrol and defer function
    @classmethod
    def enrol(cls) -> None:
        if not cls.STUDENT:
            cls.STUDENT = True
            print("Congrats! You are in")
        else:
            print("You already in")

    @classmethod
    def defer(cls) -> None:
        if cls.STUDENT:
            cls.STUDENT = False
            print("You are out see you soon")
        else:
            print("You're already out")


# If i try to instantiate the AlxSchool class i will get and error can't instantiate
# this is because it is just a blueprint for all subclass

# school = AlxSchool()
# TypeError: Can't instantiate abstract class AlxSchool with abstract methods defer, enrol


# print(student1.name)  # This will raise AttributeError cause student has not enrol

# Enrolling before instantiating
Student.enrol()
student1 = Student("Ayo", "Backend", 10)
print(student1.name)

Student.defer()
student1 = Student("Ayo", "Backend", 10)

print(student1.STUDENT)
print(student1.name)
