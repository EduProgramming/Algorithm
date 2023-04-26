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

/** 조합을 이용한 방안 */
import java.util.Scanner;

public class Main {
	
	static int N;
	static int M;
	static int[] cards;
	static int maxV;
	
	static void combi(int r, int idx, boolean[] visit) {
		if (r == 0) {
			int sumV = 0;
			for (int i=0; i<N; i++) {
				if (visit[i]) {
					sumV += cards[i];
				}
			}
			if (sumV <= M) {
				if (sumV > maxV) maxV = sumV;
			}
			return;
		}
		
		for (int i=idx; i<N; i++) {
			visit[i] = true;
			combi(r-1, i+1, visit);
			visit[i] = false;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		
		cards = new int[N];
		
		for (int i=0; i<N; i++) {
			cards[i] = sc.nextInt();
		}
		
		combi(3, 0, new boolean[N]);
		
		System.out.println(maxV);
		
		sc.close();
	}
}