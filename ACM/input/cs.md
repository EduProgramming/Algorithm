# C# 입출력

## 데이터 예제 입력이 하나일 때

> **예제 문제**
>
> [https://www.acmicpc.net/problem/5585](https://www.acmicpc.net/problem/5585)
>
> **답안 소스**
>
> [정답 소스코드](../greedy/p5585.%20%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88.cs)

### 입출력

```c#
using System;

namespace Main
{
    class Program
    {
        static void Main(String[] args)
        {
            int N = int.Parse(Console.ReadLine());

            Console.WriteLine(N); // 출력
        }
    }
}
```

## 데이터 예제 입력 여러개일 때

> **예제 문제**
>
> [https://www.acmicpc.net/problem/2798](https://www.acmicpc.net/problem/2798)
>
> **답안 소스**
>
> [정답 소스코드](../brute_force/p2798.%20%EB%B8%94%EB%9E%99%EC%9E%AD.cs)

### 입출력

```c#
using System;

namespace Main
{
    class Program
    {
        static void Main(String[] args)
        {
            int[] info = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int N = info[0];
            int M = info[1];
        }
    }
}
```
