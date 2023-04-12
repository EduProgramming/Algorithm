import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	
	static int arr[][];
	static int visited[][];
	
	static int bfs(int startRow, int startCol, int maxRow, int maxCol) {
		int[] dy = {1, 0, -1, 0};
		int[] dx = {0, 1, 0, -1};
		Queue<Integer> q = new LinkedList<>();
		q.add(startRow);
		q.add(startCol);
		visited[startRow][startCol] = 1;
		
		while (!q.isEmpty()) {
			int row = q.poll();
			int col = q.poll();
			
			for (int i=0; i < 4; i++) {
				int dRow = row + dy[i];
				int dCol = col + dx[i];
				
				if (dRow >= 0 && dRow < maxRow && dCol >= 0 && dCol < maxCol) {
					if (arr[dRow][dCol] == 2) {
						return visited[row][col] + 1;
					} else if (visited[dRow][dCol] == 0 && arr[dRow][dCol] == 1) {
						visited[dRow][dCol] = visited[row][col] + 1;
						q.add(dRow);
						q.add(dCol);
					}
				}
			}
		}
		return 0;
	}
	
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
 		
 		int N = sc.nextInt();
 		int M = sc.nextInt();
 		
 		arr = new int[N][M];
 		visited = new int[N][M];
 		
 		for(int i=0; i < N; i++) {
 			String line = sc.next();
 			for (int j=0; j < M; j++) {
 				arr[i][j] = Integer.parseInt(line.substring(j, j+1));
 			}
 		}
 		
 		arr[N-1][M-1] = 2;
 		int result = bfs(0, 0, N, M);
 		System.out.println(result);
    }
}