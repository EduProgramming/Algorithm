# T = int(input())

# for _ in range(T):
#     A, B = map(int, input().split())

#     mode = B % A
#     small = A

#     while mode > 0:
#         temp = mode
#         mode = small % mode
#         small = temp

#     print(A * B // small)

"""
재귀함수를 이용한 풀이
"""
def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    result = A * B // gcd(A, B)
    print(result)