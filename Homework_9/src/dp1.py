def solution(n):
    memo = [1] * n
    if n != 1:
        memo[1] = 2
    
    for i in range(2, n):
        memo[i] = (memo[i - 1] % 1000000007) + (memo[i - 2] % 1000000007)
    
    return memo[-1] % 1000000007


if __name__ == '__main__':
    for i in range(1, 60001):
        print(solution(i))