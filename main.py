from fastapi import FastAPI
from models import StudentModel
from student_manager import StudentManager

app = FastAPI(
    title="Student Management System API",
    description="Student Management System using FastAPI, Pandas, CSV and Faker",
    version="1.0.0"
)

manager = StudentManager()

# ==========================================
# Home
# ==========================================

@app.get("/")
def home():
    return {
        "message": "Welcome to Student Management System API"
    }


# ==========================================
# View All Students
# ==========================================

@app.get("/students")
def get_students():
    return manager.view_students()


# ==========================================
# Add Student
# ==========================================

@app.post("/students")
def add_student(student: StudentModel):
    return manager.add_student(
        student.student_id,
        student.name,
        student.age,
        student.department,
        student.cgpa
    )


# ==========================================
# Total Students
# ==========================================

@app.get("/students/total")
def total_students():
    return manager.total_students()


# ==========================================
# Topper
# ==========================================

@app.get("/students/topper")
def topper():
    return manager.topper()


# ==========================================
# Average CGPA
# ==========================================

@app.get("/students/average")
def average():
    return manager.average()


# ==========================================
# Department Wise Students
# ==========================================

@app.get("/students/departments")
def department_students():
    return manager.department_students()


# ==========================================
# Generate Fake Students
# ==========================================

@app.post("/students/faker")
def generate_fake_students():
    return manager.generate_fake_students()


# ==========================================
# Update Student
# ==========================================

@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentModel):
    return manager.update_student(
        student_id,
        student.name,
        student.age,
        student.department,
        student.cgpa
    )


# ==========================================
# Delete Student
# ==========================================

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return manager.delete_student(student_id)


# ==========================================
# Search Student
# Keep this route LAST
# ==========================================

@app.get("/students/{student_id}")
def search_student(student_id: int):
    return manager.search_student(student_id)