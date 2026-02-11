def find_grade(student):
    if student["marks"] >= 90:
        return "A"
    elif student["marks"] >= 75:
        return "B"
    else:
        return "C"


student1 = {
    "name": "Rahim",
    "marks": 82
}

grade = find_grade(student1)
print("Grade:", grade)
