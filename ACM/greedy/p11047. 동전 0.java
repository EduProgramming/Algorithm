import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int changeKind[] = new int[N];
		
		long result = 0;
		
		for (int i = 0; i < N; i++) {
			changeKind[i] = Integer.parseInt(br.readLine());
		}
		
		for (int i=N-1; i >= 0; i--) {
			int changeCnt = K / changeKind[i];
			K %= changeKind[i];
			result += changeCnt;
		}
		
		System.out.println(result);
	}
}