def solution(dartResult):
    cha = []
    digit = []
    flag = 0
    idx = 0
    for i in dartResult:
        if i.isdigit():
            if flag == 0:
                flag = 1
                digit.append(int(i))
            else:
                digit.pop()
                digit.append(10)
        else:
            flag = 0
            cha.append(i)
    for i in cha:
        if i.isalpha():
            if i == 'D':
                digit[idx] **= 2
            elif i == 'T':
                digit[idx] **= 3
        else:
            idx -= 1
            temp = idx
            if i == '*':
                digit[temp] *= 2
                if temp >= 1:
                    digit[temp - 1] *= 2
            else:
                digit[temp] *= -1
        idx += 1

    return sum(digit)