import sys

N, K = map(int, sys.stdin.readline().split())

course = list(map(int, sys.stdin.readline().split()))


length_course = sum(course)
count_course = len(course)
course_plus = course[0]
course_plus_plus = length_course 
#K의 현재 위치
point = 1
point_plus = N + 1

if K < length_course:
    for i in range(1, count_course):
        if K >= course_plus:
            point += 1
            course_plus += course[i]
        else:
            break
elif K == length_course:
    point = N

else:
    for i in range(1, count_course + 1):
        if K >= course_plus_plus:
            point_plus -= 1
            course_plus_plus += course[-i]
        else:
            point = point_plus
            break
    
print(point)