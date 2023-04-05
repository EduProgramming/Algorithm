# N = 9
# person = [0] * N

# for i in range(N):
#     person[i] = int(input())

# def selectPerson():
#     dwarf = [0] * 7
#     for i in range(N-6):
#         for j in range(i+1, N-5):
#             for k in range(j+1, N-4):
#                 for x in range(k+1, N-3):
#                     for y in range(x+1, N-2):
#                         for z in range(y+1, N-1):
#                             for m in range(z+1, N):
#                                 sumV = person[i] + person[j] + person[k] + person[x] + person[y] + person[z] + person[m]
#                                 if sumV > 100:
#                                     continue
#                                 elif sumV == 100:
#                                     dwarf[0] = person[i]
#                                     dwarf[1] = person[j]
#                                     dwarf[2] = person[k]
#                                     dwarf[3] = person[x]
#                                     dwarf[4] = person[y]
#                                     dwarf[5] = person[z]
#                                     dwarf[6] = person[m]
#                                     return dwarf

# answer = selectPerson()

# # 선택정렬 -> 더 짧게 하려면 sort함수 사용
# for i in range(len(answer)-1):
#     for j in range(i+1, len(answer)):
#         if answer[i] > answer[j]:
#             answer[i], answer[j] = answer[j], answer[i]

# for i in range(len(answer)):
#     print(answer[i])

"""
조합 풀이
: 해당하는 경우가 여러번 발생할 수 있어서
  7명 이상의 출력이 이뤄지는 경우가 있어
  boolean 값으로 처리해둠 -> 덕분에 복잡함
"""
N = 9
person = [0] * N

box = [0] * 2
person_index_box = [0] * 2

isSubmit = False

sumV = 0
for i in range(N):
    person[i] = int(input())
    sumV += person[i]

def comb(n, r):
    global isSubmit
    if r == 0:
        if not isSubmit:
            tempSumV = 0
            for i in range(len(box)):
                tempSumV += box[i]
            if sumV - tempSumV == 100:
                for i in range(len(person_index_box)):
                    person[person_index_box[i]] = 101
                
                person.sort()
                for i in range(7):
                    print(person[i])
                isSubmit = True
        else:
            return
    elif n < r:
        return
    else:
        box[r-1] = person[n-1]
        person_index_box[r-1] = n-1
        comb(n-1, r-1)
        comb(n-1, r)

comb(N, 2)