class Student:

    # instance method init
    def __init__(self, name: str, cohort: int, specialization: str) -> None:  # initialize function
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

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value
        return self.__password

    def __str__(self) -> str:
        return f"My name is {self.name}, I'm cohort in  {self.cohort:d}, My secret is{self.password}"


student1 = Student("Ayobami",  "10", "Backend")


student1.password = "New Password"

print(student1)

# print(student1.cohort)

# student1.cohort = 9  # setter

# print(student1.cohort)  # getter
