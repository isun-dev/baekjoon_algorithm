def solution(id_list, k):
    answer = 0
    arr = list()
    count = {}

    for i in id_list:
        arr.append(list(set(i.split())))

    for j in arr:
        for h in j:
            try:
                count[h] += 1
            except:
                count[h] = 1

    for key, value in count.items():
        if value > k:
            answer += k
        else:
            answer += value

    return answer