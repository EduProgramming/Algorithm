import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = 9;
		int person[] = new int[N];
		
		int sumV = 0;
		for (int i=0; i < N; i++) {
			person[i] = Integer.parseInt(br.readLine());
			sumV += person[i];
		}
		
		boolean isEnd = false;
		for (int i=0; i < N-1; i++) {
			for (int j = i+1; j < N; j++) {
				if (sumV - person[i] - person[j] == 100) {
					person[i] = -1;
					person[j] = -1;
					isEnd = true;
					break;
				}
			}
			if (isEnd) break;
		}
		
		Arrays.sort(person);
		for (int i = 2; i < N; i++) {
			System.out.println(person[i]);
		}
	}
}