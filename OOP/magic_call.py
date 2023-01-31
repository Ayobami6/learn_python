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

    def __call__(self, name, cohort, specialization):
        self.name = name
        self.cohort = cohort
        self.specialization = specialization

    def __str__(self):
        return f"Name is {self.name}, I'm in Cohort {self.cohort}, My Specialization is {self.specialization}"


student1 = Student("Ayobami", 10, "Backend")

print(student1)

student1("Bunmi", 10, "Backend")
print(student1)
