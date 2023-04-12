import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static ArrayList<Integer>[] graph;
	static boolean[] visited;
	
	static void bfs(int node) {
		visited[node] = true;
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(node);
		
		while (!q.isEmpty()) {
			int x = q.poll();
			for (int i : graph[x]) {
				if (!visited[i]) {
					visited[i] = true;
					q.add(i);
				}
			}
		}
	}
	
	static void dfs(int node) {
		if (visited[node]) return;
		
		visited[node] = true;
		for (int i : graph[node]) {
			if (!visited[i])
				dfs(i);
		}
	}
	
    public static void main(String[] args) {
 		Scanner sc = new Scanner(System.in);
 		int N = sc.nextInt();
 		int M = sc.nextInt();
 		
 		graph = new ArrayList[N+1];
 		visited = new boolean[N+1];
 		
 		for (int i=1; i < N+1; i++) {
 			graph[i] = new ArrayList<Integer>();
 		}
 		
 		for (int i=0; i < M; i++) {
 			int start = sc.nextInt();
 			int end = sc.nextInt();
 			
 			graph[start].add(end);
 			graph[end].add(start);
 		}
 		
 		int cnt = 0;
 		for (int i=1; i < N+1; i++) {
 			if (!visited[i]) {
 				cnt++;
// 				dfs(i);
 				bfs(i);
 			}
 		}
 		
 		System.out.println(cnt);
    }
}