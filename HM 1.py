
grades = [78, 92, 65, 92, 81, 74, 99, 67, 88, 99]
grade2 = grades.copy()

grades.sort()
print(grades)

count = 0
while count < 3:
    print(max(grade2))
    count += 1
    grade2.remove(max(grade2))

grades.sort(reverse=True)
print(grades)

count = 0
while count < 3:
    print(min(grade2))
    count += 1
    grade2.remove(min(grade2))