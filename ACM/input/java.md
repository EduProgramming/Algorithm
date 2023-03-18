# Java 입출력

## 데이터 예제 입력이 하나일 때

> **예제 문제**
>
> [https://www.acmicpc.net/problem/5585](https://www.acmicpc.net/problem/5585)
>
> **답안 소스**
>
> [정답 소스코드](../greedy/p5585.%20%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88.java)

### Scanner 사용

```java
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		System.out.println(N); // 출력
        sc.close();
	}
}
```

### BufferedReader 사용

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        System.out.println(N); // 출력
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
> [정답 소스코드](../brute_force/p2798.%20%EB%B8%94%EB%9E%99%EC%9E%AD.java)

### Scanner 사용

```java
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		int[] array = new int[N];

		for (int i=0; i < N; i++) {
			array[i] = sc.nextInt();
		}

		sc.close();
	}
}
```

### BufferedReader 사용

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] array = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i < N; i++) {
        	array[i] = Integer.parseInt(st.nextToken());
        }
	}
}
```
