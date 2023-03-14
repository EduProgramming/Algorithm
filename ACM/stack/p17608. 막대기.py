"""
import sys
input = sys.stdin.readline
사용해야하는 문제로 보임
"""

import sys
input = sys.stdin.readline

N = int(input())

stack = [0] * N

for i in range(N):
    stack[i] = int(input())

cnt = 0
maxV = 0
for i in range(N-1, -1, -1):
    if maxV < stack[i]:
        maxV = stack[i]
        cnt += 1

print(cnt)