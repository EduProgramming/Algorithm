import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data = br.readLine();
		String[] splitData = data.split("-");
		
		long result = 0;
		boolean isStart = false;
		for (int i=0; i < splitData.length; i++) {
            // [+] -> https://fmaker7.tistory.com/109
            // 컴파일러가 +를 인식하지 못하여 특수문자라고 알려줘야함
            // \\+라고 쓰거나 [+]라고 사용해야함
            // *, $, | 도 동일
            // 괄호도 동일
			String[] plusSplitData = splitData[i].split("[+]");
			for (int j=0; j < plusSplitData.length; j++) {
				if (!isStart) {
					result += Integer.parseInt(plusSplitData[j]);
				} else {
					result -= Integer.parseInt(plusSplitData[j]);
				}
			}
			isStart = true;
		}
		System.out.println(result);
	}
}
