import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int money = 1000 - Integer.parseInt(br.readLine());
		int startExchangeMoney = 500;
		
		boolean isSwitch = false;
		long result = 0;
		
		while (startExchangeMoney > 0) {
			int exchangeCnt = money / startExchangeMoney;
			money = money - (startExchangeMoney * exchangeCnt);
			result += exchangeCnt;
			
			isSwitch = !isSwitch;
			if (isSwitch) {
				startExchangeMoney /= 5;
			} else {
				startExchangeMoney /= 2;
			}
		}
		
		System.out.println(result);
	}
}
