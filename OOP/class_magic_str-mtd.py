# Magic String methods
# __str__: used to generate strings, mostly used to print str to stdou
# __repr__: Also str function, mostly used for debugging purposes, more developer friendly
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

    # Overwriting the __str__ function
    def __str__(self):
        return f"Name is {self.name} from cohort {self.cohort}"

    # Overwriting the __repr__ function
    def __repr__(self):
        return f"Name={self.name}, from={self.cohort}"


# student object instantiation
student1 = Student("Ayobami", "10")

print(student1)  # Before overwriting the __str__ function this will print
# out the address location of the object
print(student1.cohort)
# Calling the functions on the object
print(str(student1))
print(repr(student1))
