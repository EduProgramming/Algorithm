# Java에서는 substring 사용해야함

N = list(input())

# 선택 정렬
for i in range(len(N)-1):
    for j in range(i+1, len(N)):
        if N[i] < N[j]:
            N[i], N[j] = N[j], N[i]

# # 버블 정렬
# for i in range(len(N)-1):
#     for j in range(len(N)-i-1):
#         if N[j] < N[j+1]:
#             N[j], N[j+1] = N[j+1], N[j]

result = ''.join(N)
print(result)