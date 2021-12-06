# dictionary를 value 기준으로 정렬하기 위한 라이브러리
from operator import itemgetter

def solution2(N, stages):
    # stages의 최대 값이 N + 1 이기 때문에, N + 1 개의 0을 가진 lst 생성
    lst = [0 for i in range(N+1)]

    # lst의 인덱스 = stages의 값인 lst에 + 1
    for stage in stages:
        lst[stage-1] += 1

    # 실패율을 나타내기 위해 해당 위치부터 끝까지 더한 값을 나눔
    for i in range(len(lst) - 1):
        # 0으로 나누는 경우 제외
        if sum(lst[i:]):
            lst[i] /= sum(lst[i:])

    # lst N+1 번째 수는 모든 스테이지를 통과한 사람의 실패율이므로 나타낼 필요가 없음
    lst= lst[0:N]

    # dictionary의 key값으로 사용하기 위한 리스트 keys 선언
    # keys = [1, 2, 3, 4, 5...]
    keys = [x+1 for x in range(N)]

    # result = {
    #       1 : lst[0],
    #       2 : lst[1],
    #       3 : lst[2], ...
    # }  의 dictoinary 생성
    result = dict(zip(keys, lst))

    # itemgetter(0) : key 기준 정렬
    # itemgetter(1) : value 기준 정렬
    # slist = [(1, lst[0]), (2, lst[1]) ...] 형태의 리스트가 되며 value 기준으로 내림차순 정렬 한다.
    slist= sorted(result.items(), key=itemgetter(1), reverse=True)

    # slist 의 key(?)만 뽑아낸 리스트 answer
    answer = [x[0] for x in slist]
    return answer



