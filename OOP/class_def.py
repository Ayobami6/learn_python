# Basic class definition

class Student:
    def __init__(self, name, cohort) -> None:  # initialize function
        """ instance initialization function

        Args:
            name (str): name of student
            cohort (int): student cohort

        Returns:
                None
        """
        self.name = name
        self.cohort = cohort


# student object instantiation
student1 = Student("Ayobami", "10")

print(student1)
print(student1.cohort)
