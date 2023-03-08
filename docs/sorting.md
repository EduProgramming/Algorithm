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
