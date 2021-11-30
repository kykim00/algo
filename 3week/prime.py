# 소수 판별

def is_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# 3가지 수를 어떻게 뽑아내야 하나 고민하다 답을 못찾고 3중 for문 으로....

def solution(nums):
    result = 0
    length = len(nums)
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                sum = nums[i] + nums[j] + nums[k]
                if is_prime(sum):
                    result += 1
    return result


# 잘 쓰여진 다른 사람의 코드
# combination(nums, 3) 으로 3가지 수의 조합을 모두 찾아내었다.

def solution2(nums):
    from itertools import combinations
    return sum([is_prime(sum(c)) for c in combinations(nums,3)])
