import sys
input = sys.stdin.readline

K = int(input())

stack = [0] * K

for i in range(K):
    stack[i] = int(input())

remove_count = 0
result = 0

for i in range(K-1, -1, -1):
    if stack[i] == 0:
        remove_count += 1
        continue
    elif remove_count > 0:
        remove_count -= 1
        continue

    result += stack[i]

print(result)