import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int L = -1;
		int P = -1;
		int V = -1;
		
		int idx = 0;
		
		while (true) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			L = Integer.parseInt(st.nextToken());
			P = Integer.parseInt(st.nextToken());
			V = Integer.parseInt(st.nextToken());
			
			int result = 0;
			
			if (L + P + V == 0)
				break;
			
			idx++;
			
			int minDay = (V % P) > L ? L : (V % P);
			result = (V / P) * L + minDay;
			
			System.out.println("Case " + idx + ": " + result);
		}
	}
}
