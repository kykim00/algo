def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        # sign is true
        if sign:
            answer += num
        else:
            answer -= num
    return answer