import math

N, M = map(int, input().split())

search_idx = 10**7

search_idx = M + 1 if M+1 < search_idx else search_idx + 1

is_prime_number = [True] * (search_idx)
is_prime_number[0] = False
is_prime_number[1] = False

for i in range(2, int(math.sqrt(search_idx)) + 1):
    if is_prime_number[i]:
        for j in range(2*i, search_idx, i):
            is_prime_number[j] = False


cnt = 0
search_range = int(math.sqrt(M)) + 1
for i in range(2, search_range):
    if is_prime_number[i]:
        value = i
        idx = 2
        while value <= M:
            value = i ** idx
            idx += 1
            if value <= M and value >= N:
                cnt += 1

print(cnt)