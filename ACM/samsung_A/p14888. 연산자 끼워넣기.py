def f(s, idx, plus, minus, mul, div):
    global maxV, minV
    if idx == N:
        if minV > s:
            minV = s
        if maxV < s:
            maxV = s
    else:
        if plus:
            f(s + A[idx], idx+1, plus-1, minus, mul, div)
        if minus:
            f(s - A[idx], idx+1, plus, minus-1, mul, div)
        if mul:
            f(s * A[idx], idx+1, plus, minus, mul-1, div)
        if div:
            f(int(s / A[idx]), idx+1, plus, minus, mul, div-1)

N = int(input())
A = list(map(int, input().split()))
operator_list = list(map(int, input().split()))
maxV = -1000000000
minV = 1000000000

f(A[0], 1, operator_list[0], operator_list[1], operator_list[2], operator_list[3])
print(maxV)
print(minV)