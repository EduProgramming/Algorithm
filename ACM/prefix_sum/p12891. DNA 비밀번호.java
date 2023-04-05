import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int getSpell(char spell) {
		int result = -1;
		switch(spell) {
			case 'A': {
				result = 0;
				break;
			}
			case 'C': {
				result = 1;
				break;
			}
			case 'G': {
				result = 2;
				break;
			}
			case 'T': {
				result = 3;
				break;
			}
		}
		return result;
	}
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        
        char[] DNA = new char[S];
        DNA = br.readLine().toCharArray();
        
        st = new StringTokenizer(br.readLine());
        int[] check = new int[4]; // A C G T
        for (int i=0; i<4; i++) {
        	check[i] = Integer.parseInt(st.nextToken());
        }
        
        int start = 0;
        int end = P-1;
        int cnt = 0;
        
        char before = DNA[0];
        
        int[] countSpell = new int[4];
    	for (int i=start; i <= end; i++) {
    		int result = getSpell(DNA[i]);
    		if (result >= 0) {
    			countSpell[result]++;
    		}
    	}
        
        while (end < S) {
        	
        	boolean isOk = true;
        	for (int i=0; i < 4; i++) {
        		if (check[i] > countSpell[i]) {
        			isOk = false;
        			break;
        		}
        	}
        	
        	if (isOk) cnt++;
        	
        	start++;
        	end++;
        	
        	int removeIdx = getSpell(before);
        	if (removeIdx >= 0) {
        		countSpell[removeIdx]--;
        	}
        	
        	if (end >= S) break;
        	
        	before = DNA[start];
        	int result = getSpell(DNA[end]);
        	if (result >= 0) {
        		countSpell[result]++;
        	}
        }
        
        System.out.println(cnt);
    }
}