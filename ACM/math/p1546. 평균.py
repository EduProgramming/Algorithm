N = input()
score_list = list(map(int, input().split()))

M = score_list[0]
sumScore = score_list[0]

subject_number = len(score_list)

for idx in range(1, subject_number):
    sumScore += score_list[idx]
    M = score_list[idx] if score_list[idx] > M else M

result = sumScore * 100 / M / subject_number

print(result)