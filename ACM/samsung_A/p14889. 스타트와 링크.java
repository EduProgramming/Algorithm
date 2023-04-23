import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	
	static int[][] S;
	static int[] INDEX_LIST;
	static int[] box;
	static int[][] startTeamList;
	static int startTeamIdx;
	
	static int[] twoBox;
	static long startTeamSum;
	static long linkTeamSum;
	
	static void combi(int n, int r) {
		if (r == 0) {
			for (int i=0; i<box.length; i++) {
				startTeamList[startTeamIdx][i] = box[i];
			}
			startTeamIdx++;
		} else if (n < r) {
			return;
		} else {
			box[r-1] = INDEX_LIST[n-1];
			combi(n-1, r-1);
			combi(n-1, r);
		}
	}
	
	static void combiSum(int n, int r, int[] arr, boolean isHome) {
		if (r == 0) {
			if (isHome) {
				startTeamSum += S[twoBox[0]][twoBox[1]];
				startTeamSum += S[twoBox[1]][twoBox[0]];
			} else {
				linkTeamSum += S[twoBox[0]][twoBox[1]];
				linkTeamSum += S[twoBox[1]][twoBox[0]];
			}
		} else if (n < r) {
			return;
		} else {
			twoBox[r-1] = arr[n-1];
			combiSum(n-1, r-1, arr, isHome);
			combiSum(n-1, r, arr, isHome);
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		S = new int[N][N];
		INDEX_LIST = new int[N];
		
		for (int i=0; i<N; i++) {
			INDEX_LIST[i] = i;
		}
		
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				S[i][j] = sc.nextInt();
			}
		}
		int halfN = N / 2;
		int combiSize;
		int combination[][] = new int[21][21];
		combination[1][0] = 1;
		combination[1][1] = 1;
		for (int i=1; i<N+1; i++) {
			for (int j=0; j<i+1; j++) {
				if (j == 0) {
					combination[i][j] = 1;
				} else if (i == j) {
					combination[i][j] = 1;
				} else {
					combination[i][j] = combination[i-1][j-1] + combination[i-1][j];
				}
			}
		}
		combiSize = combination[N][halfN];
		startTeamList = new int[combiSize][halfN];
		
		box = new int[halfN];
		
		combi(N, halfN);
		
		Arrays.sort(startTeamList, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				for (int i=0; i< o1.length; i++) {
					if (o1[i] != o2[i]) {
						return o1[i] - o2[i];
					}
				}
				// 끝번호까지 같다? Woops
				return o1[0] - o2[0];
			}
			
		});
		
		int TWO_NUM = 2;
		twoBox = new int[TWO_NUM];
		
		long minV = Long.MAX_VALUE;
		for (int i=0; i<startTeamList.length; i++) {
			startTeamSum = 0;
			linkTeamSum = 0;
			combiSum(startTeamList[i].length, TWO_NUM, startTeamList[i], true);
			int[] linkTeamList = startTeamList[startTeamList.length - i -1];
			combiSum(startTeamList[i].length, TWO_NUM, linkTeamList, false);
			if (Math.abs(startTeamSum - linkTeamSum) < minV) {
				minV = Math.abs(startTeamSum - linkTeamSum);
			}
		}
		
		System.out.println(minV);
		
		sc.close();
	}
}