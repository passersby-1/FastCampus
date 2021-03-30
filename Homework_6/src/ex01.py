def solution(s):
    s = [int(x) for x in s.split()]
    answer = f'{min(s)} {max(s)}'
    return answer


print(solution("1 2 3 4"))