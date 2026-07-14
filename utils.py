def validate_student_id(student_id):
    try:
        student_id = int(student_id)
        return student_id > 0
    except (ValueError, TypeError):
        return False


def validate_age(age):
    try:
        age = int(age)
        return 18 <= age <= 30
    except (ValueError, TypeError):
        return False


def validate_cgpa(cgpa):
    try:
        cgpa = float(cgpa)
        return 0 <= cgpa <= 4
    except (ValueError, TypeError):
        return False