# 셀프 넘버
# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의
# 에 따라 함수를 정의한다.

# set으로 중복되는 숫자 제거

# 10000 이하까지 for 문을 돌리면서
# s_set에 add 하고 차집합 기능을 이용해서
# 셀프넘버 출력

def d(n):
    x = 0 # 초기화
    a = list(str(n)) # 문자열 분할
    for i in a:
        x = x + int(i) # 분리한 값 더하기
    return n + x # 파라미터와 더하기


s_set = set()  # set 에 담아서 중복으로 값 저장되지 않도록 하기
for k in range(1, 10001):
    s_set.add(d(k))  #  set 에 담기
result = set(range(1, 10001)) - s_set  #  set 차집합 사용해서 한꺼번에 삭제.
for num in sorted(result):  # 오름차순 정렬
    print(num)
