def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)
    

A, B = map(int, input().split())

result = gcd(A, B)

for i in range(result):
    print(1, end="")