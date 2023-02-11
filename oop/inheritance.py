# Defining the base class
class AlxSchool:
    def __init__(self, name: str, specialization: str, p) -> None:
        self.name = name
        self.specialization = specialization
        self.__p = p


# Student inheriting from AlxSchool base class
class Student(AlxSchool):
    def __init__(self, name: str, specialization: str, cohort: int, p) -> None:  # initialize function
        """ instance initialization function

        Args:
            name (str): name of student
            cohort (int): student cohort

        Returns:
                None
        """
        # Calling the super class init funtion to access base class instance
        # attributes
        # You don't need to parse self
        AlxSchool.__init__(self, name, specialization, p)
        self.cohort = cohort

    def say_hello(self):
        print(f"Hello {self._AlxSchool__p}")


# Mentor inheriting from AlxSchool


class Mentor(AlxSchool):
    def __init__(self, name: str, specialization: str, department: str, p) -> None:
        AlxSchool.__init__(self, name, specialization, p)
        self.department = department


# instantiation
mentor1 = Mentor("Leykun", "Backend", "Technical", "p")
student1 = Student("Caroline", "Frontend", 10, "p")

student1.say_hello()
print(mentor1.name)
print(f"My name is {student1.name} I'm from cohort {student1.cohort}")
