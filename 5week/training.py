def solution(n, lost, reserve):
    # 인원 수 만큼의 배열 선언, 1로 초기화
    pos = [1 for _ in range(n)]
    # 여벌이 있는 사람은 + 1
    for i in reserve:
        pos[i-1] += 1
    # 도난 당한 사람 - 1
    for i in lost:
        pos[i-1] -= 1
    # 여벌 없이 도난당한 사람 = 0 
    # case 별로 나누어 처리
    for i in range(len(pos)):
        if pos[i] == 0:
            if i == 0:
                if pos[i+1] == 2:
                    pos[i+1] -= 1
                    pos[i] += 1
            elif i == len(pos)-1:
                if pos[i-1] == 2:
                    pos[i-1] -= 1
                    pos[i] += 1
            else:
                if pos[i-1] == 2:
                    pos[i-1] -= 1
                    pos[i] += 1
                elif pos[i+1] == 2:
                    pos[i+1] -= 1
                    pos[i] += 1
    return pos.count(1) + pos.count(2)


# 잘 작성된 다른사람의 코드
# 나중에 추가된 테스트케이스 2가지에서 실패가 나지만 도움이 될 것같다.

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
