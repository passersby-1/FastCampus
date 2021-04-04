def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    answer = distance
    l, r = 0, distance
    while l <= r:
        mid = (l + r) // 2
        start = 0
        removed_rock = 0

        min_n = float('inf')
        for rock in rocks:
            if rock - start < mid:
                removed_rock += 1
            else:
                min_n = min(min_n, rock-start)
                start = rock

        if n < removed_rock:
            r = mid - 1
        else:
            answer = min_n
            l = mid + 1

    return answer


if __name__ == '__main__':
    print(solution(25, [2, 14, 11, 21, 17], 2))
    # print(solution(25, [2, 14, 11, 21, 17], 5))
    # print(solution(1025, [2, 14, 11, 21, 17, 30, 100, 999], 8))
    # print(solution(25, [2], 1))