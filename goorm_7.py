# 369게임

num = int(input())
count = 0
arr_num = []
arr = [3, 6, 9]

for i in range(1, num):
    check = list(map(int, str(i)))
    for j in range(len(check)):
        if check[j] in arr:
            count = count + 1
print(count)

