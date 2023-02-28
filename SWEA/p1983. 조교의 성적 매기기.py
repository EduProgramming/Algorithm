import sys
sys.stdin = open("p1983. 조교의 성적 매기기.txt", "r")

GRADE_LIST = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    duplication_num = N // 10
    score_list = []
    search_score = -1
    for score_case in range(1, N+1):
        midterm, final, assignment = map(int, input().split())
        score = (midterm * 0.35) + (final * 0.45) + (assignment * 0.2)
        score_list.append(score)
        if score_case == K:
            search_score = score
    score_list.sort(reverse=True)
    idx = score_list.index(search_score)
    result = GRADE_LIST[idx // duplication_num]
    print(f'#{test_case} {result}')