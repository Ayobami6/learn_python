# Defining the base class
class AlxSchool:
    def __init__(self, name: str, specialization: str) -> None:
        self.name = name
        self.specialization = specialization


class Database:
    def __init__(self, cohort: int, id: int) -> None:
        self.cohort = cohort
        self.id = id


# Student inheriting from AlxSchool and Database
class Student(AlxSchool, Database):
    def __init__(self, name: str, specialization: str, cohort: int, id: int) -> None:  # initialize function
        """ instance initialization function

        Args:
            name (str): name of student
            cohort (int): student cohort

        Returns:
                None
        """
        # Calling the base classess init function to access their attributes
        AlxSchool.__init__(self, name, specialization)
        Database.__init__(self, cohort, id)

    def showattr(self):
        print(self.name)
        print(self.specialization)
        print(self.cohort)
        print(self.id)


student1 = Student("Wisdom", "Backend", 10, 16548)

print(student1.id)

student1.showattr()
print(Student.__mro__)  # the magic method mro (method resolution order)
# gets the order of class method or attr implementation
