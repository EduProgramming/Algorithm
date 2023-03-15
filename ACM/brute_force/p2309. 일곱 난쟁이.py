N = 9
person = [0] * N

for i in range(N):
    person[i] = int(input())

def selectPerson():
    dwarf = [0] * 7
    for i in range(N-6):
        for j in range(i+1, N-5):
            for k in range(j+1, N-4):
                for x in range(k+1, N-3):
                    for y in range(x+1, N-2):
                        for z in range(y+1, N-1):
                            for m in range(z+1, N):
                                sumV = person[i] + person[j] + person[k] + person[x] + person[y] + person[z] + person[m]
                                if sumV > 100:
                                    continue
                                elif sumV == 100:
                                    dwarf[0] = person[i]
                                    dwarf[1] = person[j]
                                    dwarf[2] = person[k]
                                    dwarf[3] = person[x]
                                    dwarf[4] = person[y]
                                    dwarf[5] = person[z]
                                    dwarf[6] = person[m]
                                    return dwarf

answer = selectPerson()

# 선택정렬 -> 더 짧게 하려면 sort함수 사용
for i in range(len(answer)-1):
    for j in range(i+1, len(answer)):
        if answer[i] > answer[j]:
            answer[i], answer[j] = answer[j], answer[i]

for i in range(len(answer)):
    print(answer[i])