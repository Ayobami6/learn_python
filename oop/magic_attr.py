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

    def __str__(self):
        return f"Name is {self.name}, I'm in Cohort {self.cohort}, My password is {self.__password}"

    def __getattribute__(self, name):
        if name == "password":
            password = super().__getattribute__("_Student__password")
            return password
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "password":
            self.__password = value
            return super().__setattr__(name, value)
        return super().__setattr__(name, value)

    def __getattr__(self, name):
        return f"{name} is not an attribute"


student1 = Student("Ayobami", 10, "Backend")

print(student1.password)

student1.password = "New Password"

print(student1.password)

print(student1.pas)
