"""
L과 P의 관계에서 min 생각해야함
"""

L, P, V = -1, -1, -1
test_index = 0

while True:
    L, P, V = map(int, input().split())
    # if (L == 0 and P == 0 and V == 0):
    if (L + P + V == 0): # 이러한 방도도 있음
        break
    test_index += 1
        
    result = (V // P * L) + min((V % P), L)
    
    print(f'Case {test_index}: {result}')