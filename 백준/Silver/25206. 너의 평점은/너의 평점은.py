total_num = total_grade = 0
for _ in range(20):
    name, num, grade = input().split()
    num = float(num)
    if grade == 'A+':
        grade = 4.5
    elif grade == 'A0':
        grade = 4.0
    elif grade == 'B+':
        grade = 3.5
    elif grade == 'B0':
        grade = 3.0
    elif grade == 'C+':
        grade = 2.5
    elif grade == 'C0':
        grade = 2.0
    elif grade == 'D+':
        grade = 1.5
    elif grade == 'D0':
        grade = 1.0
    elif grade == 'F':
        grade = 0.0
    elif grade == 'P':
        continue
    total_num += num
    total_grade += num * grade
print('%.6f'%(total_grade/total_num))