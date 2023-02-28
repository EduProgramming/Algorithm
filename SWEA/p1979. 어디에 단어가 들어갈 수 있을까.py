import sys
sys.stdin = open("p1979. 어디에 단어가 들어갈 수 있을까.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    array_list = [0 for _ in range(N)]
    cnt = K

    result = 0
    for idx in range(N):
        array_list[idx] = list(map(int, input().split()))

    for row in range(N):
        cnt = 0
        for col in range(N):
            if array_list[row][col] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    for row in range(N):
        cnt = 0
        for col in range(N):
            if array_list[col][row] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    print(f'#{t} {result}')