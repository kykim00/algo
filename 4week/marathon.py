# 정확성 100%, 효율성 0% 시간초과 => 문제 분류인 해시로 접근

def solution_first(participant, completion):
    for comp in completion:
        if comp in participant:
            participant.remove(comp)
    return participant[0]

# 통과
def solution(participant, completion):
    dic = dict()
    for part in participant:
        if part in dic.keys():
            dic[part] += 1
        else:
            dic[part] = 1
    for comp in completion:
        dic[comp] -= 1
    answer = [k for k, v in dic.items() if v == 1]
    return answer[0]

# 엄청난 풀이 1

# counter로 participant, completion dictionary를 각각 생성하고 빼기
# counter 객체는 뺄셈이 가능하다.... wow
import collections

def solution_wonder1(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 엄청난 풀이 2

# 이게 진짜 해시다... 
def solution_wonder2(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += hash(part)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer