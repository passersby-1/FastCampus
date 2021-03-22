def solution(N, stages):
    players = len(stages)
    
    floor = [stages.count(x) for x in range(1, N + 1)]
    clear = []
    for i, v in enumerate(floor):
        if players != 0:
            clear.append((i + 1, v / players))
        else:
            clear.append((i + 1, players))
        players -= v
    ans = [x[0] for x in sorted(clear, key=lambda x : (-x[1], x[0]))]

    return ans
