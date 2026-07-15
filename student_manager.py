from student import Student
from file_handler import FileHandler
from faker import Faker
import random
import pandas as pd

from utils import (
    validate_student_id,
    validate_age,
    validate_cgpa
)


class StudentManager:

    def __init__(self):

        self.file = FileHandler()
        self.fake = Faker()

    # ==========================================
    # Add Student
    # ==========================================
    def add_student(self):

        student_id = input("Enter Student ID : ")

        if not validate_student_id(student_id):
            print("Invalid Student ID! ID must be greater than 0.")
            return

        df = self.file.read_file()

        if student_id in df["ID"].astype(str).values:
            print("Student ID Already Exists!")
            return

        name = input("Enter Name : ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        age = input("Enter Age : ")

        if not validate_age(age):
            print("Invalid Age! Age must be between 18 and 30.")
            return

        age = int(age)

        department = input("Enter Department : ").strip()

        if not department:
            print("Department cannot be empty.")
            return

        cgpa = input("Enter CGPA (0 - 4): ")

        if not validate_cgpa(cgpa):
            print("Invalid CGPA!")
            return

        cgpa = float(cgpa)

        student = Student(
            student_id,
            name,
            age,
            department,
            cgpa
        )

        df.loc[len(df)] = student.to_dict()

        self.file.save_file(df)

        print("Student Added Successfully.")

    # ==========================================
    # View Students
    # ==========================================
    def view_students(self):

        df = self.file.read_file()

        if df.empty:

            print("No Students Found.")

        else:

            print(df)

    # ==========================================
    # Search Student
    # ==========================================
    def search_student(self):

        student_id = input("Enter Student ID : ")

        if not validate_student_id(student_id):
            print("Invalid Student ID!")
            return

        df = self.file.read_file()

        result = df[df["ID"].astype(str) == student_id]

        if result.empty:

            print("Student Not Found.")

        else:

            print(result)

    # ==========================================
    # Delete Student
    # ==========================================
    def delete_student(self):

        student_id = input("Enter Student ID : ")

        if not validate_student_id(student_id):
            print("Invalid Student ID!")
            return

        df = self.file.read_file()

        if student_id not in df["ID"].astype(str).values:

            print("Student Not Found.")

            return

        df = df[df["ID"].astype(str) != student_id]

        self.file.save_file(df)

        print("Student Deleted Successfully.")
            # ==========================================
    # Update Student
    # ==========================================
    def update_student(self):

        student_id = input("Enter Student ID : ")

        if not validate_student_id(student_id):
            print("Invalid Student ID!")
            return

        df = self.file.read_file()

        if student_id not in df["ID"].astype(str).values:

            print("Student Not Found.")
            return

        index = df[df["ID"].astype(str) == student_id].index[0]

        print("\nLeave blank if you don't want to update.\n")

        name = input("New Name : ").strip()
        age = input("New Age : ").strip()
        department = input("New Department : ").strip()
        cgpa = input("New CGPA : ").strip()

        if name:
            df.loc[index, "Name"] = name

        if age:

            if not validate_age(age):
                print("Invalid Age! Age must be between 18 and 30.")
                return

            df.loc[index, "Age"] = int(age)

        if department:
            df.loc[index, "Department"] = department

        if cgpa:

            if not validate_cgpa(cgpa):
                print("Invalid CGPA! CGPA must be between 0 and 4.")
                return

            df.loc[index, "CGPA"] = float(cgpa)

        self.file.save_file(df)

        print("Student Updated Successfully.")

    # ==========================================
    # Total Students
    # ==========================================
    def total_students(self):

        df = self.file.read_file()

        print("\nTotal Students :", len(df))

    # ==========================================
    # Topper
    # ==========================================
    def topper(self):

        df = self.file.read_file()

        if df.empty:

            print("No Students Found.")
            return

        highest = df["CGPA"].max()

        print("\nTopper Student:\n")

        print(df[df["CGPA"] == highest])

    # ==========================================
    # Average CGPA
    # ==========================================
    def average(self):

        df = self.file.read_file()

        if df.empty:

            print("No Students Found.")
            return

        average_cgpa = round(df["CGPA"].mean(), 2)

        print(f"\nAverage CGPA : {average_cgpa}")