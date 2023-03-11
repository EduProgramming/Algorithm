# 정렬 알고리즘

## 선택 정렬

```python
for i in range(N-1):
    for j in range(i+1, N):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
```

## 버블 정렬

```python
for i in range(N-1):
    for j in range(N-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
```

## 삽입 정렬

```python
for i in range(1, N):
    key = array[i]
    for j in range(i-1, -1, -1):
        if key < array[j]:
            array[j], array[j+1] = array[j+1], array[j]
        else:
            break
```

## 퀵 정렬

```python
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = []
    right = []
    for i in range(1, len(array)):
        if pivot > array[i]:
            left.append(array[i])
        else:
            right.append(array[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
```
