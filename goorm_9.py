# 세로 순서 사각형
num = int(input())

for i in range(1, num + 1):
    count = 0
    for _ in range(1, num + 1):
        print(i + num * count, end=' ')
        count += 1
    print()
