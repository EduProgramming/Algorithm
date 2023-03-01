"""
해당 방안에서는 읽는 부분(input)을 조금 빠르게
처리하는 방안을 상요해야 PASS가 나옴.

그게 아니라면 pypy로 언어를 선택해서 진행해야함.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))

S = [0] * (N+1)

for i in range(N):
    S[i+1] = S[i] + array[i]

result = [0] * M
for i in range(M):
    start_index, end_index = map(int, input().split())
    result[i] = S[end_index] - S[start_index-1]

for i in range(len(result)):
    print(result[i])