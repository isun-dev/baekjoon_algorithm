# 시험성적 평균과 등급 구하기

korean, math, english = map(int, input().split())
average = (korean + math + english) / 3
if average >= 90:
    grade = 'A'
elif 80 <= average < 90:
    grade = 'B'
elif 70 <= average < 80:
    grade = 'C'
elif 60 <= average < 70:
    grade = 'D'
else:
    grade = 'F'

print(format(average, ".2f"), grade)
