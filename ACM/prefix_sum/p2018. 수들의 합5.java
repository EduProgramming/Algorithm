import java.util.Scanner;

public class Main {
	
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int N = sc.nextInt();
        int arr[] = new int[N];
        
        for (int i=0; i < N; i++) {
        	arr[i] = i+1;
        }
        
        int start = 0;
        int end = 0;
        int cnt = 0;
        
        while (end < N) {
        	
        	int sumV = 0;
        	for (int i=start; i <= end; i++) {
				// 해당 부분 줄여서 성능Up 할수 있음
        		sumV += arr[i];
        	}
        	
        	if (sumV > N) start++;
        	else if (sumV == N) {
        		cnt++;
        		end++;
        	} else {
        		end++;
        	}
        }
        
        System.out.println(cnt);
    }
}