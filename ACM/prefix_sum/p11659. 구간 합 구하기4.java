import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        int arr[] = new int[N];
        for (int i=0; i<N; i++) {
        	arr[i] = sc.nextInt();
        }
        
        int dp[] = new int[N+1];
        for (int i=0; i<N; i++) {
        	dp[i+1] = dp[i] + arr[i];
        }
        
        for (int i=0; i<M; i++) {
        	int start = sc.nextInt();
        	int end = sc.nextInt();
        	System.out.println(dp[end] - dp[start-1]);
        }
        
        sc.close();
    }
}