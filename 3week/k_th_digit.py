def solution(array, commands):
    answer= []
    for li in commands:
        answer.append(sorted(array[li[0] - 1: li[1]])[li[2] - 1])
    return answer