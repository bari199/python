def average_marks(marks_dict):
    total = sum(marks_dict.values())
    count = len(marks_dict)
    average = total / count
    return average


# Dictionary
marks = {
    "Math": 80,
    "Science": 75,
    "English": 85,
    "Computer": 90
}

result = average_marks(marks)
print("Average marks:", result)
