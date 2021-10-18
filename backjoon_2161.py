n = int(input())
a = [i for i in range(1, n+1)]

while len(a) > 1:
    print(a.pop(0), end=' ')
    k = a.pop(0)
    a.append(k)
print(a[0])