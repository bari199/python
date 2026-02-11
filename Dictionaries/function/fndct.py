def highest_marks(students):
    top_student = ""
    max_marks = 0

    for name, marks in students.items():
        if marks > max_marks:
            max_marks = marks
            top_student = name

    return top_student, max_marks


students = {
    "Ayan": 78,
    "Riya": 92,
    "Kabir": 85
}

name, marks = highest_marks(students)
print("Top student:", name)
print("Marks:", marks)
