# Basic class definition
# Pillars Of OOP
# 1. Encapsulation
# 2. Inheritance
# 3. Abstraction
# 4. Polymorphysism


class Student:

    def __init__(self, names, cohorts) -> None:  # initialize function
        """ instance initialization function

        Args:
            name (str): name of student
            cohort (int): student cohort

        Returns:
                None
        """
        self.name = names
        self.cohort = cohorts


# student object instantiation
student1 = Student("Ayo", 10)
student2 = Student("Bunmi", 9)
print(student1)
print(student2.cohort, student1.name)
# print(student1.name)
# print(help(student1))
