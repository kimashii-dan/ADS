ratings = {
    "A+": 4.0,
    "A": 3.75,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0
}

def quick_sort(students):
    if len(students) <= 1:
        return students
    else:
        pivot = students[len(students) // 2]['gpa']
        left = [student for student in students if student['gpa'] < pivot]
        middle = [student for student in students if student['gpa'] == pivot]
        right = [student for student in students if student['gpa'] > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def gpa(grades):

    total_points = 0
    total_credits = 0
    for i in range(0, len(grades), 2):
        credit = int(grades[i + 1])
        letter = grades[i]
        grade = ratings[letter]
        total_points += grade * credit
        total_credits  += credit
    
    return total_points / total_credits


students = []
n = int(input())
for i in range(n):
    first, last, amount, *grades = input().split()
    student = {
        "first_name": first,
        "last_name": last,
        "subject_amount": int(amount),
        "grades": grades,
        "gpa": round(gpa(grades), 3)
    }
    students.append(student)

sorted_students = quick_sort(students)

for student in sorted_students:
    print("{first} {last} {gpa:.3f}".format(first = student["first_name"], last = student["last_name"], gpa = student["gpa"]))
    