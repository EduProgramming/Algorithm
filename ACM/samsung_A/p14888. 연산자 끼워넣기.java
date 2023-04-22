import java.util.Scanner;

public class Main {
	
	static int N;
	static long minV = 1000000000;
	static long maxV = -1000000000;
	static int[] A;
	static int[] OP;
	
	static void f(long s, int idx, int plus, int minus, int mul, int div) {
		if (idx == N) {
			if (minV > s) minV = s;
			if (maxV < s) maxV = s;
		} else {
			if (plus > 0) {
				f(s + A[idx], idx + 1, plus - 1, minus, mul, div);
			}
			if (minus > 0) {
				f(s - A[idx], idx + 1, plus, minus - 1, mul, div);
			}
			if (mul > 0) {
				f(s * A[idx], idx + 1, plus, minus, mul - 1, div);
			}
			if (div > 0) {
				f((long) s / A[idx], idx + 1, plus, minus, mul, div-1);
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		A = new int[N];
		for (int i=0; i<N; i++) {
			A[i] = sc.nextInt();
		}
		OP = new int[4];
		for (int i=0; i<OP.length; i++) {
			OP[i] = sc.nextInt();
		}
		
		f(A[0], 1, OP[0], OP[1], OP[2], OP[3]);
		
		System.out.println(maxV);
		System.out.println(minV);
	}
}