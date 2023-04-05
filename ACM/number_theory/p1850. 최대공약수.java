import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        long N = sc.nextLong();
        long M = sc.nextLong();
        
        long small = N;
        long mode = M % N;
        
        while (mode > 0) {
        	long temp = mode;
        	mode = small % mode;
        	small = temp;      	
        }
        
        for (int i=0; i < small; i++) {
        	bw.write("1");
        }
        
        bw.flush();
        bw.close();
        sc.close();
    }
}