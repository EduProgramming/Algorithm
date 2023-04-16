import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	
static ArrayList<Integer>[] graph;
static int[] tree;

static void bfs(int node) {
	Queue<Integer> q = new LinkedList();
	q.add(node);
	
	while (!q.isEmpty()) {
		int x = q.poll();
		
		if (tree[x] != -1) {
			for (int i=0; i < graph[tree[x]].size(); i++) {
				if (x == graph[tree[x]].get(i)) {
					graph[tree[x]].remove(i);
				}
			}
		}
		
		for (int i : graph[x]) {
			q.add(i);
		}
		graph[x].add(-1);
	}
}
	
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int N = sc.nextInt();
    	graph = new ArrayList[N];
    	for (int i=0; i < N; i++) {
    		graph[i] = new ArrayList();
    	}
    	tree = new int[N];
    	
    	for (int i=0; i < N; i++) {
    		tree[i] = sc.nextInt();
    		
    		if (tree[i] == -1)
    			continue;
    		graph[tree[i]].add(i);
    	}
    	
    	int R = sc.nextInt();
    	
    	bfs(R);
    	
    	int cnt = 0;
    	for (int i=0; i < graph.length; i++) {
    		if (graph[i].isEmpty())
    			cnt++;
    	}
    	System.out.println(cnt);
    }
}