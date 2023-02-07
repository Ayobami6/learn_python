# Magic Equality and comparison methods
# __eq__: equality
# __ge__: greater or equal
# __lt__: less than
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

    # overwriting the magic methods
    def __eq__(self, other) -> bool:
        if not isinstance(other, Student):
            raise ValueError("Not a student")
        return (self.name == other.name and self.cohort == other.cohort)

    def __ge__(self, other):
        return (self.cohort >= other.cohort)

    # TODO:
    # __le__ and __lt__


student1 = Student("Ayobami", 10)
student2 = Student("Rizzy", 9)
student3 = Student("Ayobami", 10)

print(student1 == student3)

print(student1 >= student3)
# This will raise an error cause 4 is not an instance of Student
print(student1 == 4)

print(student1 == student3)
