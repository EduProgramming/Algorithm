import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        boolean isPrime[] = new boolean[M+1];
        for (int i=2; i < M+1; i++) {
        	isPrime[i] = true;
        }
        
        for (int i=2; i < M+1; i++) {
        	if (isPrime[i]) {
        		for (int j=2*i; j < M+1; j+=i) {
        			isPrime[j] = false;
        		}
        	}
        }
        
        for (int i=N; i < M+1; i++) {
        	if (isPrime[i])
        		System.out.println(i);
        }
        
        sc.close();
    }
}