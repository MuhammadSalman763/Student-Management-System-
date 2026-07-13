from student import Student
from file_handler import FileHandler
from faker import Faker
import random
import pandas as pd


class StudentManager:

    def __init__(self):

        self.file = FileHandler()
        self.fake = Faker()

    # ==========================================
    # Add Student
    # ==========================================
    def add_student(self):

        try:

            student_id = input("Enter Student ID : ")

            df = self.file.read_file()

            if student_id in df["ID"].astype(str).values:
                print("Student ID Already Exists!")
                return

            name = input("Enter Name : ")

            age = int(input("Enter Age : "))

            department = input("Enter Department : ")

            while True:

                try:

                    cgpa = float(input("Enter CGPA (0 - 4): "))

                    if 0 <= cgpa <= 4:
                        break

                    print("CGPA must be between 0 and 4.")

                except ValueError:

                    print("Invalid CGPA.")

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

        except ValueError:

            print("Age must be an integer.")

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

        df = self.file.read_file()

        if student_id not in df["ID"].astype(str).values:

            print("Student Not Found.")

            return

        index = df[df["ID"].astype(str) == student_id].index[0]

        print("\nLeave blank if you don't want to update.\n")

        name = input("New Name : ")

        age = input("New Age : ")

        department = input("New Department : ")

        cgpa = input("New CGPA : ")

        if name:

            df.loc[index, "Name"] = name

        if age:

            df.loc[index, "Age"] = int(age)

        if department:

            df.loc[index, "Department"] = department

        if cgpa:

            cgpa = float(cgpa)

            if 0 <= cgpa <= 4:

                df.loc[index, "CGPA"] = cgpa

            else:

                print("Invalid CGPA")

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

        print(df[df["CGPA"] == highest])

    # ==========================================
    # Average CGPA
    # ==========================================
    def average(self):

        df = self.file.read_file()

        if df.empty:

            print("No Students Found.")

            return

        print("Average CGPA :", round(df["CGPA"].mean(), 2))

    # ==========================================
    # Department Wise Students
    # ==========================================
    def department_students(self):

        df = self.file.read_file()

        if df.empty:

            print("No Students Found.")

            return

        print(df.groupby("Department").size())

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

        print("1000 Fake Students Generated Successfully.")