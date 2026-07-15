from pydantic import BaseModel, Field


class StudentModel(BaseModel):

    student_id: int = Field(..., gt=0)

    name: str

    age: int = Field(..., ge=18, le=100)

    department: str

    cgpa: float = Field(..., ge=0.0, le=4.0)