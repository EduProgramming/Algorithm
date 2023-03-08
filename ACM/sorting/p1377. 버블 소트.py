"""
bool changed = false;
for (int i=1; i<=N+1; i++) {
    changed = false;
    for (int j=1; j<=N-i; j++) {
        if (A[j] > A[j+1]) {
            changed = true;
            swap(A[j], A[j+1]);
        }
    }
    if (changed == false) {
        cout << i << '\n';
        break;
    }
}

출력하고자하는 값:
전체 정렬이 완성되는 횟수 출력
1회차라고 생각해서 시작

[주의점]
1 <= N <= 500,000 | 시간 제한: 2초
O(N^2) 방법으로는 제한에 걸림
O(NlogN) 방법을 찾아야함

해당 문제는 빠른 방안을 고려하여도
```python
import sys
input = sys.stdin.readline
```
를 사용해야 풀이가 되었음
"""
import sys
input = sys.stdin.readline

N = int(input())

A = [[0, i] for i in range(N)]

for i in range(N):
    A[i][0] = int(input())

A.sort(key= lambda x : x[0])

max_num = 0

for i in range(len(A)):
    idx = A[i][1] - i
    max_num = idx if idx > max_num else max_num

print(max_num + 1)