class Student:

    def __init__(
        self,
        student_id: int,
        name: str,
        age: int,
        department: str,
        cgpa: float
    ):

        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa

    def to_dict(self):

        return {

            "ID": self.student_id,

            "Name": self.name,

            "Age": self.age,

            "Department": self.department,

            "CGPA": self.cgpa

        }