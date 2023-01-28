# Basic class definition

class Student:

    # instance method init
    def __init__(self, name, cohort, specialization) -> None:  # initialize function
        """ instance initialization function

        Args:
            name (str): name of student
            cohort (int): student cohort

        Returns:
                None
        """
        # these are instance attributes or properties
        self.name = name
        self.cohort = cohort
        self.specialization = specialization
        # this is a private instance attribute
        self.__password = "This is my password"

    # Instance methon getname to get name of student

    def getname(self) -> str:
        return self.name

    def getcohort(self) -> int:
        # Since the _newcohort attribute was not defined during the instance
        # init We need to check if the object has the attr with hasattr functions
        if hasattr(self, "_newcohort"):
            return self._newcohort
        else:
            return self.cohort

    def changecohort(self, cohort) -> None:
        # the underscore newcohort means the attribute newcohort is internal to
        # the class should be access internally only
        self._newcohort = cohort


student1 = Student("Ayobami", 10, "Backend")

print(student1.getcohort())
student1.changecohort(9)
print(student1.getcohort())

# Accessing the private attribute password
print(student1.__password)  # Will get AttributeError no such attribute
# This is because python as prefix the __password attribute with the class name
# Which is called name mangling to prevent subclasses to overwrite the attribute
print(student1._Student__password)  # This will print out the password
