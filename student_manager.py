from student import Student
from file_handler import FileHandler
from faker import Faker
import pandas as pd
import random


class StudentManager:

    def __init__(self):

        self.file = FileHandler()
        self.fake = Faker()

    # ==========================================
    # Add Student
    # ==========================================

    def add_student(self, student_id, name, age, department, cgpa):

        df = self.file.read_file()

        if student_id in df["ID"].astype(str).values:
            return {
                "success": False,
                "message": "Student ID Already Exists"
            }

        if cgpa < 0 or cgpa > 4:
            return {
                "success": False,
                "message": "CGPA must be between 0 and 4"
            }

        student = Student(
            student_id,
            name,
            age,
            department,
            cgpa
        )

        df.loc[len(df)] = student.to_dict()

        self.file.save_file(df)

        return {
            "success": True,
            "message": "Student Added Successfully"
        }

    # ==========================================
    # View Students
    # ==========================================

    def view_students(self):

        df = self.file.read_file()

        if df.empty:

            return []

        return df.to_dict(orient="records")

    # ==========================================
    # Search Student
    # ==========================================

    def search_student(self, student_id):

        df = self.file.read_file()

        result = df[df["ID"].astype(str) == student_id]

        if result.empty:

            return {
                "success": False,
                "message": "Student Not Found"
            }

        return result.to_dict(orient="records")

    # ==========================================
    # Delete Student
    # ==========================================

    def delete_student(self, student_id):

        df = self.file.read_file()

        if student_id not in df["ID"].astype(str).values:

            return {
                "success": False,
                "message": "Student Not Found"
            }

        df = df[df["ID"].astype(str) != student_id]

        self.file.save_file(df)

        return {
            "success": True,
            "message": "Student Deleted Successfully"
        }
        # ==========================================
    # Update Student
    # ==========================================

    def update_student(self, student_id, name=None, age=None, department=None, cgpa=None):

        df = self.file.read_file()

        if student_id not in df["ID"].astype(str).values:

            return {
                "success": False,
                "message": "Student Not Found"
            }

        index = df[df["ID"].astype(str) == student_id].index[0]

        if name is not None:
            df.loc[index, "Name"] = name

        if age is not None:
            df.loc[index, "Age"] = age

        if department is not None:
            df.loc[index, "Department"] = department

        if cgpa is not None:

            if cgpa < 0 or cgpa > 4:

                return {
                    "success": False,
                    "message": "CGPA must be between 0 and 4"
                }

            df.loc[index, "CGPA"] = cgpa

        self.file.save_file(df)

        return {
            "success": True,
            "message": "Student Updated Successfully"
        }

    # ==========================================
    # Total Students
    # ==========================================

    def total_students(self):

        df = self.file.read_file()

        return {
            "Total Students": len(df)
        }

    # ==========================================
    # Topper
    # ==========================================

    def topper(self):

        df = self.file.read_file()

        if df.empty:

            return {
                "message": "No Students Found"
            }

        highest = df["CGPA"].max()

        topper = df[df["CGPA"] == highest]

        return topper.to_dict(orient="records")

    # ==========================================
    # Average CGPA
    # ==========================================

    def average(self):

        df = self.file.read_file()

        if df.empty:

            return {
                "Average CGPA": 0
            }

        return {
            "Average CGPA": round(df["CGPA"].mean(), 2)
        }

    # ==========================================
    # Department Wise Students
    # ==========================================

    def department_students(self):

        df = self.file.read_file()

        if df.empty:

            return {}

        result = df.groupby("Department").size()

        return result.to_dict()

    # ==========================================
    # Generate 1000 Fake Students
    # ==========================================

    def generate_fake_students(self):

        df = self.file.read_file()

        departments = [
            "Computer Science",
            "Software Engineering",
            "Information Technology",
            "Artificial Intelligence",
            "Cyber Security",
            "Data Science",
            "Business Administration",
            "Electrical Engineering"
        ]

        if df.empty:

            next_id = 1

        else:

            next_id = int(df["ID"].astype(int).max()) + 1

        students = []

        for i in range(1000):

            student = Student(

                str(next_id + i),

                self.fake.name(),

                random.randint(18, 25),

                random.choice(departments),

                round(random.uniform(2.00, 4.00), 2)

            )

            students.append(student.to_dict())

        new_df = pd.DataFrame(students)

        df = pd.concat([df, new_df], ignore_index=True)

        self.file.save_file(df)

        return {
            "success": True,
            "message": "1000 Fake Students Generated Successfully"
        }
    