N = int(input())

array = [0] * N

for idx in range(N):
    array[idx] = int(input())

"""
[방법1] 버블정렬
"""
def bubble_sorting():
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

"""
[방법2] 선택정렬
"""
def select_sorting():
    for i in range(N-1):
        for j in range(i+1, N):
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp

# bubble_sorting() # 버블정렬
# select_sorting() # 선택정렬


for i in range(N):
    print(array[i])
