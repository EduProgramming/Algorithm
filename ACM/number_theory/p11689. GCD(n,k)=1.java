import java.util.Scanner;

public class Main {
	
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	long N = sc.nextLong();
    	
    	long result = N;
    	
    	for (int i=2; i < Math.sqrt(N) + 1; i++) {
    		if (N % i == 0) {
    			result = result - result / i;
    		}
    		while (N % i == 0) {
    			N = N / i;
    		}
    	}
    	
    	if (N > 1) {
    		result = result - result / N;
    	}
    	System.out.println(result);
    	sc.close();
    }
}