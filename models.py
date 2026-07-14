from pydantic import BaseModel, Field


class StudentModel(BaseModel):

    student_id: str
    name: str
    age: int = Field(..., ge=18, le=30)
    department: str
    cgpa: float = Field(..., ge=0.0, le=4.0)