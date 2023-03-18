# Python 입출력

> **참고사항**
>
> 백준 Python 문제에서 입출력 속도가 간소한 차이로 실패하는 경우가 있음
>
> 이러한 경우에는 다음과 같이 해결해볼 수도 있음
>
> 아래의 소스를 가장 상위에 작성해주면 됨

```python
import sys
input = sys.stdin.readline
```

## 데이터 예제 입력이 하나일 때

> **예제 문제**
>
> [https://www.acmicpc.net/problem/5585](https://www.acmicpc.net/problem/5585)
>
> **답안 소스**
>
> [정답 소스코드](../greedy/p5585.%20%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88.py)

### 입출력

```python
N = int(input())

print(N) # 출력
```

## 데이터 예제 입력 여러개일 때

> **예제 문제**
>
> [https://www.acmicpc.net/problem/2798](https://www.acmicpc.net/problem/2798)
>
> **답안 소스**
>
> [정답 소스코드](../brute_force/p2798.%20%EB%B8%94%EB%9E%99%EC%9E%AD.py)

### 입출력

```python
N, M = map(int, input().split())
array = list(map(int, input().split()))
```
