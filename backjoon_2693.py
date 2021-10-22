T = int(input())

for _ in range(T):
    number = list(map(int, input().split()))
    number.sort(reverse=True)
    print(number[2])