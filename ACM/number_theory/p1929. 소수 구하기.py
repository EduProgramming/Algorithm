N, M = map(int, input().split())

is_prime_number = [True] * (M+1)
is_prime_number[0] = False
is_prime_number[1] = False

for i in range(2, M+1):
    if is_prime_number[i]:
        for j in range(2*i, M+1, i):
            is_prime_number[j] = False

for i in range(N, M+1):
    if is_prime_number[i]:
        print(i)