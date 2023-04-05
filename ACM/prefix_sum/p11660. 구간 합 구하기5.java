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
    	int arr[][] = new int[N][N];
        int DP[][] = new int[N+1][N+1];
        
        for (int i=0; i < N; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j=0; j < N; j++) {
        		arr[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        
        for (int i=1; i < N+1; i++) {
        	for (int j=1; j < N+1; j++) {
        		DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + arr[i-1][j-1];
        	}
        }
        
        for (int i=0; i < M; i++) {
        	st = new StringTokenizer(br.readLine());
        	int row1 = Integer.parseInt(st.nextToken());
        	int col1 = Integer.parseInt(st.nextToken());
        	int row2 = Integer.parseInt(st.nextToken());
        	int col2 = Integer.parseInt(st.nextToken());
        	
        	System.out.println(DP[row2][col2] - DP[row1-1][col2] - DP[row2][col1-1] + DP[row1-1][col1-1]);
        }
        
        br.close();
    }
}