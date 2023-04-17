import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	
	static long[] tree;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int K = sc.nextInt();
		
		long MIN_NUM = Long.MIN_VALUE;
		long MAX_NUM = Long.MAX_VALUE;
		
		int k = 0;
		while (N > (int) Math.pow(2, k)) {
			k++;
		}
		
		// 2 ** 19 = 524,288
		// 2 ** 20 = 1,048,576
		// 2 ** 21 = 2,097,152
		// int 범위 = -2,147,483,648 ~ 2,147,483,647
		int treeSize = (int) Math.pow(2, k+1);
		tree = new long[treeSize];
		
		int dataStartIdx = treeSize / 2;
		// 입력으로 주어지는 모든 수는 long타입 범위
		for (int i=0; i < N; i++) {
			tree[dataStartIdx + i] = sc.nextLong();
		}
		
		int tempStartIdx = dataStartIdx;
		int tempCnt = treeSize / 4;
		
		while (tempCnt > 0) {
			int parentIdx = tempStartIdx / 2;
			for (int i=0; i < tempCnt; i++) {
				tree[parentIdx + i] = tree[tempStartIdx + 2*i] + tree[tempStartIdx + 2*i + 1];
			}
			tempCnt = tempCnt / 2;
			tempStartIdx = tempStartIdx / 2;
		}
		
		for (int i=0; i < M+K; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			long c = sc.nextLong();
			
			int startIndex = dataStartIdx + b - 1;
			if (a == 1) {
				tree[startIndex] = c;
				int parentIdx = startIndex / 2;
				while (parentIdx >= 1) {
					int leftChildIdx = parentIdx * 2;
					int rightChildIdx = leftChildIdx + 1;
					tree[parentIdx] = tree[leftChildIdx] + tree[rightChildIdx];
					parentIdx = parentIdx / 2;
				}
			} else {
				int endIndex = dataStartIdx + (int) c - 1;
				ArrayList<Long> pocket = new ArrayList<Long>();
				while (endIndex >= startIndex) {
					if (startIndex % 2 == 1) {
						pocket.add(tree[startIndex]);
					}
					if (endIndex % 2 == 0) {
						pocket.add(tree[endIndex]);
					}
					startIndex = (startIndex + 1) / 2;
					endIndex = (endIndex - 1) / 2;
				}
				
				long prefixSum = 0;
				for (long element : pocket) {
					prefixSum += element;
				}
				if (prefixSum > MAX_NUM) prefixSum = MAX_NUM;
				else if (prefixSum < MIN_NUM) prefixSum = MIN_NUM;
				
				System.out.println(prefixSum);
			}
		}
	}
}