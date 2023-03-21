import sys
sys.stdin = open("./input_data/p1204. 최빈수 구하기.txt", "r")

T = int(input())

for _ in range(T):
    t = int(input())
    num_list = list(map(int, input().split()))
    score_list = [0] * 101

    for i in range(len(num_list)):
        score_list[num_list[i]] += 1
    
    maxIndex = 0
    targetNum = 0
    for i in range(len(score_list)):
        if maxIndex <= score_list[i]:
            maxIndex = score_list[i]
            targetNum = i
    
    print(f'#{t} {targetNum}')