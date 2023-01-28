# Defining the base class
class AlxSchool:
    def __init__(self, name: str, specialization: str) -> None:
        self.name = name
        self.specialization = specialization


# Student inheriting from AlxSchool base class
class Student(AlxSchool):
    def __init__(self, name: str, specialization: str, cohort: int) -> None:  # initialize function
        """ instance initialization function

        Args:
            name (str): name of student
            cohort (int): student cohort

        Returns:
                None
        """
        # Calling the super class init funtion to access base class instance
        # attributes
        super().__init__(name, specialization)  # You don't need to parse self
        self.cohort = cohort


# Mentor inheriting from AlxSchool


class Mentor(AlxSchool):
    def __init__(self, name: str, specialization: str, department: str) -> None:
        super().__init__(name, specialization)
        self.department = department


# instantiation
mentor1 = Mentor("Leykun", "Backend", "Technical")
student1 = Student("Caroline", "Frontend", 10)

print(mentor1.name)
print(f"My name is {student1.name} I'm from cohort {student1.cohort}")
