# Custom ratings to GPA points
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

def calculate_gpa(grades_credits):
    total_points = 0
    total_credits = 0
    for grade, credit in grades_credits:
        gpa = ratings[grade]
        total_points += gpa * credit
        total_credits += credit
    return total_points / total_credits if total_credits != 0 else 0

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if (x[2], x[0], x[1]) < (pivot[2], pivot[0], pivot[1])]
    middle = [x for x in arr if (x[2], x[0], x[1]) == (pivot[2], pivot[0], pivot[1])]
    right = [x for x in arr if (x[2], x[0], x[1]) > (pivot[2], pivot[0], pivot[1])]
    return quicksort(left) + middle + quicksort(right)


n = int(input())
students = []

for _ in range(n):
    data = input().split()
    last_name = data[0]
    first_name = data[1]
    m = int(data[2])
    grades_credits = [(data[i], int(data[i + 1])) for i in range(3, 2 + 2 * m, 2)]
    gpa = calculate_gpa(grades_credits)
    students.append((last_name, first_name, gpa))


sorted_students = quicksort(students)

for student in sorted_students:
    print(f"{student[0]} {student[1]} {student[2]:.3f}")
