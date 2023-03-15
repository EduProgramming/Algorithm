"""
가장 처음과 마지막 문자는 숫자 -> 앞에 수는 무조건 양수
"""

V = input()

splitV = V.split('-')

isStart = False
result = 0

def sum_calc(arr: list) -> int:
    sumV = 0
    splitArr = arr.split('+')
    for i in range(len(splitArr)):
        sumV += int(splitArr[i])
    return sumV

for i in range(len(splitV)):
    if not isStart:
        isStart = True
        result = sum_calc(splitV[i])
    else:
        result -= sum_calc(splitV[i])

print(result)