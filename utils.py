def validate_id(student_id):
    return student_id > 0


def validate_age(age):
    return 18 <= age <= 100


def validate_cgpa(cgpa):
    return 0 <= cgpa <= 4