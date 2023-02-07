# Class definition using type annotations

class Student:
    def __init__(self, name: str, cohort: int) -> None:

        # object instance initialization
        self.name = name
        self.cohort = cohort


# Oject instantiation
student1 = Student("Ayobami", 10)

print(student1.__doc__)
