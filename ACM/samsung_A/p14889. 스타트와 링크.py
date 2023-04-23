def combi(n, r):
    if r == 0:
        temp = []
        for i in range(len(box)):
            temp.append(box[i])
        start_team_list.append(temp)
    elif n < r:
        return
    else:
        box[r-1] = INDEX_LIST[n-1]
        combi(n-1, r-1)
        combi(n-1, r)

def combi_sum(n, r, arr, is_home):
    global start_team_sum, link_team_sum
    if r == 0:
        if is_home:
            start_team_sum += S[two_box[0]][two_box[1]]
            start_team_sum += S[two_box[1]][two_box[0]]
        else:
            link_team_sum += S[two_box[0]][two_box[1]]
            link_team_sum += S[two_box[1]][two_box[0]]
    elif n < r:
        return
    else:
        two_box[r-1] = arr[n-1]
        combi_sum(n-1, r-1, arr, is_home)
        combi_sum(n-1, r, arr, is_home)

N = int(input())
S = [0 for _ in range(N)]
INDEX_LIST = [i for i in range(N)]
box = [0 for _ in range(N // 2)]

start_team_list = []

for i in range(N):
    S[i] = list(map(int, input().split()))

combi(N, len(box))

start_team_list.sort()

TWO_NUM = 2
two_box = [0 for _ in range(TWO_NUM)]

minV = 9876543210
start_team_sum = 0
link_team_sum = 0
for i in range(len(start_team_list)):
    start_team_sum = 0
    link_team_sum = 0
    combi_sum(len(start_team_list[i]), TWO_NUM, start_team_list[i], True)
    link_team = start_team_list[len(start_team_list) - i - 1]
    combi_sum(len(start_team_list[i]), TWO_NUM, link_team, False)
    if abs(start_team_sum - link_team_sum) < minV:
        minV = abs(start_team_sum - link_team_sum)

print(minV)