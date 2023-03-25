# 완전 탐색

## 순열

```python
def perm(n, k):
    if n == k:
        print(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]
```

## 부분집합

## 조합

```python
def comb(n, r):
    if r == 0:
        print(box)
    elif n < r:
        return
    else:
        box[r-1] = arr[n-1]
        comb(n-1, r-1)
        comb(n-1, r)
```
