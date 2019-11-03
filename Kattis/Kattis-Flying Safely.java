import java.util.*;
import java.util.LinkedList;

public class FlyingSafely {
    public static class Graph {
        public int V; // No. of vertices
        public LinkedList<Integer> start; // reference to the start of breath-first search
        public int startIndex;
        int maxEdge = 1;
        public LinkedList<Integer> adj[];


        // Constructor
        public Graph(int v) {
            V = v;
            adj = new LinkedList[v];
            for (int i = 0; i < v; ++i)
                adj[i] = new LinkedList();
        }


        // Function to add an edge into the graph
        void addEdge(int v, int w) {
            v -= 1;
            w -= 1;
            // undirected graph
            adj[v].add(w);
            adj[w].add(v);
            if (adj[v].size() > maxEdge) {
                start = adj[v];
                maxEdge = adj[v].size();
                startIndex = v;
            }
            if (adj[w].size() > maxEdge) {
                start = adj[w];
                maxEdge = adj[w].size();
                startIndex = w;
            }
        }


        public int getMin(int s) {
            int count = -1;
            boolean visited[] = new boolean[V];
            LinkedList<Integer> queue = new LinkedList<Integer>();
            visited[s] = true;
            queue.add(s);
            count++;

            while (queue.size() != 0) {
                // Dequeue a vertex from queue and print it
                s = queue.poll();
                // Get all adjacent vertices of the dequeued vertex s
                // If a adjacent has not been visited, then mark it
                // visited and enqueue it
                Iterator<Integer> i = adj[s].listIterator();
                while (i.hasNext()) {
                    int n = i.next();
                    if (!visited[n]) {
                        visited[n] = true;
                        queue.add(n);
                        count++;
                    }
                }
            }
            return count;
        }

    }


    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int testCase = in.nextInt();
        in.nextLine();
        Graph g = null;
        while (testCase > 0) {
            int cities = in.nextInt();
            int pilots = in.nextInt();
            in.nextLine();
            g = new Graph(cities);
            while (pilots > 0) {
                int from = in.nextInt();
                int to = in.nextInt();
                g.addEdge(from, to);
                in.nextLine();
                pilots--;
            }
            System.out.println(g.getMin(g.startIndex));
            testCase--;
        }
    }
}
