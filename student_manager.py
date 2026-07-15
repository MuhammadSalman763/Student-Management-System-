from student import Student
from file_handler import FileHandler
from utils import validate_id, validate_age, validate_cgpa
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

        # Validate Student ID
        if not validate_id(student_id):

            return {
                "success": False,
                "message": "Student ID must be greater than 0."
            }

        # Duplicate ID
        if student_id in df["ID"].astype(int).values:

            return {
                "success": False,
                "message": "Student ID already exists."
            }

        # Validate Age
        if not validate_age(age):

            return {
                "success": False,
                "message": "Age must be between 18 and 30."
            }

        # Validate CGPA
        if not validate_cgpa(cgpa):

            return {
                "success": False,
                "message": "CGPA must be between 0 and 4."
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
            "message": "Student added successfully.",
            "student": student.to_dict()
        }

    # ==========================================
    # View Students
    # ==========================================
    def view_students(self):

        df = self.file.read_file()

        if df.empty:

            return {
                "message": "No students found.",
                "students": []
            }

        return df.to_dict(orient="records")

    # ==========================================
    # Search Student
    # ==========================================
    def search_student(self, student_id):

        df = self.file.read_file()

        result = df[df["ID"].astype(int) == student_id]

        if result.empty:

            return {
                "success": False,
                "message": "Student not found."
            }

        return result.to_dict(orient="records")[0]
        # ==========================================
    # Delete Student
    # ==========================================
    def delete_student(self, student_id):

        df = self.file.read_file()

        if student_id not in df["ID"].astype(int).values:

            return {
                "success": False,
                "message": "Student not found."
            }

        df = df[df["ID"].astype(int) != student_id]

        self.file.save_file(df)

        return {
            "success": True,
            "message": "Student deleted successfully."
        }

    # ==========================================
    # Update Student
    # ==========================================
    def update_student(self, student_id, name, age, department, cgpa):

        df = self.file.read_file()

        if student_id not in df["ID"].astype(int).values:

            return {
                "success": False,
                "message": "Student not found."
            }

        if not validate_age(age):

            return {
                "success": False,
                "message": "Age must be between 18 and 30."
            }

        if not validate_cgpa(cgpa):

            return {
                "success": False,
                "message": "CGPA must be between 0 and 4."
            }

        index = df[df["ID"].astype(int) == student_id].index[0]

        df.loc[index, "Name"] = name
        df.loc[index, "Age"] = age
        df.loc[index, "Department"] = department
        df.loc[index, "CGPA"] = cgpa

        self.file.save_file(df)

        return {
            "success": True,
            "message": "Student updated successfully."
        }

    # ==========================================
    # Total Students
    # ==========================================
    def total_students(self):

        df = self.file.read_file()

        return {
            "total_students": len(df)
        }

    # ==========================================
    # Topper
    # ==========================================
    def topper(self):

        df = self.file.read_file()

        if df.empty:

            return {
                "message": "No students found."
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
                "message": "No students found."
            }

        return {
            "average_cgpa": round(df["CGPA"].mean(), 2)
        }

    # ==========================================
    # Department Wise Students
    # ==========================================
    def department_students(self):

        df = self.file.read_file()

        if df.empty:

            return {
                "message": "No students found."
            }

        department_count = (
            df.groupby("Department")
            .size()
            .reset_index(name="Total Students")
        )

        return department_count.to_dict(orient="records")

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
            next_id = int(df["ID"].max()) + 1

        students = []

        for i in range(1000):

            student = Student(
                next_id + i,
                self.fake.name(),
                random.randint(18, 30),
                random.choice(departments),
                round(random.uniform(2.00, 4.00), 2)
            )

            students.append(student.to_dict())

        new_df = pd.DataFrame(students)

        df = pd.concat([df, new_df], ignore_index=True)

        self.file.save_file(df)

        return {
            "success": True,
            "message": "1000 fake students generated successfully.",
            "total_added": 1000
        }