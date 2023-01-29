from typing import Optional

"""_summary_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """


class Student:
    SPECIALIZATION = ("Backend", "Frontend")

    # private class attribute
    __students: Optional[list] = None

    # Creating a class method using the classmethod decorator
    @classmethod
    def getspecs(cls) -> tuple:
        return cls.SPECIALIZATION

    # using static method to create student list with singleton design patter
    @staticmethod
    def getstudentlist() -> Optional[list]:
        if Student.__students is None:
            Student.__students = []
        return Student.__students

    def __init__(self, name, spec) -> None:  # initialize function
        """ instance initialization function

        Args:
            name (str): name of student
            cohort (int): student cohort

        Returns:
                None
        """
        self.name = name
        # checking if spec is in Class attribute Specialization
        if spec not in Student.SPECIALIZATION:
            raise ValueError(f"{spec} is invalid")
        else:
            self.spec = spec

    def __str__(self):
        return f"Student name is {self.name} and Spec is {self.spec}"

    def getstudentdetails(self):
        return dict(name=self.name, spec=self.spec)


# Getting the available specs
print("Available specialization: ", Student.getspecs())


# Instantiatizing with invalid specs
# This will raise an error so comment
# it out before run
# student2 = Student("Bunmi", "Full Stack")


student1 = Student("Ayobami", "Backend")
student3 = Student("Bunmi", "Frontend")

studentlist = Student.getstudentlist()

students = [student1, student3]

for student in students:
    studentlist.append(student.getstudentdetails())

print(studentlist)
print(student1)
