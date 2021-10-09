import sys
from collections import deque

N = int(input())
times = []
for _ in range(N):
    time = tuple(map(int,sys.stdin.readline().split()))
    times.append(time)

# 회의가 빨리 끝나는 순
# 두번째 기준은 회의 시작시간
times.sort(key= lambda x: (x[1], x[0]))
times = deque(times)

count = 1
end = times[0][1]
times.popleft() # 가장 빨리 끝나는 회의 선택

while(times):
    # 시작시간이 end보다 大 或者같을 경우 채택
    if times[0][0] >= end:
        end = times[0][1]
        times.popleft()
        count += 1
    else:
        times.popleft()

print(count)