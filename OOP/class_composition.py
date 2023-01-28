from typing import Optional
# Using Composition concept to put entities or attributes into seperate class

# Defining the base class


class AlxSchool:
    def __init__(self, name: str, specialization: str, StudentDetails: Optional[object] = None) -> None:
        self.name = name
        self.specialization = specialization
        self.StudentDetails = StudentDetails

    def getstudentdetails(self):
        return f"Name is:{self.name} Spec is:{self.specialization} {self.StudentDetails}"


class StudentDetails:
    def __init__(self, cohort: int, id: int) -> None:
        self.cohort = cohort
        self.id = id

    def __str__(self) -> str:
        return f"Cohort is:{self.cohort} and ID is:{self.id}"


# Student inheriting from AlxSchool
class Student(AlxSchool):
    def __init__(self, name: str, specialization: str, StudentDetails: object) -> None:  # initialize function
        """ instance initialization function

        Args:
            name (str): name of student
            cohort (int): student cohort

        Returns:
                None
        """
        super().__init__(name, specialization, StudentDetails)


# Instantiating for student details: cohort and Id
stdd1 = StudentDetails(10, 1567)


student1 = Student("Ayo", "Backend", stdd1)

print(student1.StudentDetails)

print(student1.getstudentdetails())
