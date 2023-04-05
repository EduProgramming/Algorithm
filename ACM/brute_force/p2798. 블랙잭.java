// import java.io.BufferedReader;
// import java.io.InputStreamReader;
// import java.util.StringTokenizer;

// public class Main {

// 	public static void main(String[] args) throws Exception {
// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 		StringTokenizer st = new StringTokenizer(br.readLine());
		
// 		int N = Integer.parseInt(st.nextToken());
// 		int M = Integer.parseInt(st.nextToken());
		
// 		int CARD_LIST[] = new int[N];
// 		int result = 0;
		
// 		st = new StringTokenizer(br.readLine());
// 		for (int i = 0; i < N; i++) {
// 			CARD_LIST[i] = Integer.parseInt(st.nextToken());
// 		}
		
// 		for (int i = 0; i < N-2; i++) {
// 			for (int j = i+1; j < N-1; j++) {
// 				for (int k = j+1; k < N; k++) {
// 					int cardSum = CARD_LIST[i] + CARD_LIST[j] + CARD_LIST[k];
// 					if (cardSum > M) {
// 						continue;
// 					} else if (cardSum <= M) {
// 						if (result < cardSum) {
// 							result = cardSum;
// 						}
// 					}
// 				}
// 			}
// 		}
// 		System.out.println(result);
// 	}
// }

/** 조합을 이용한 방안
 * 기존 알고 있던 조합 형식이 아닌
 * Java 알고리즘 구현자들이 풀이한 방식으로 따라해봄
 */
import java.util.Scanner;

public class Main {

	static int[] arr;
	
	static int maxV;
	
	static void combi(int idx, int cnt, int[] arr, boolean[] visited, int N, int R, int M) {
		if (cnt == R) {
			int sumV = 0;
			for (int i=0; i <N; i++) {
				if (visited[i]) {
					sumV += arr[i];
				}
			}
			if (sumV > M) {
				return;
			} else if (sumV > maxV) {
				maxV = sumV;
			}
			return;
		}
		
		if (idx == N) return;
		
		visited[idx] = true;
		combi(idx+1, cnt+1, arr, visited, N, R, M);
		visited[idx] = false;
		combi(idx+1, cnt, arr, visited, N, R, M);
	}
		
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int R = 3;
		int M = sc.nextInt();
		
		arr = new int[N];
		
		for (int i=0; i<N; i++) {
			arr[i] = sc.nextInt();
		}
		
		combi(0, 0, arr, new boolean[N], N, R, M);
		
		System.out.println(maxV);
		
		sc.close();
	}
}