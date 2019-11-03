import java.util.*;

public class Mravi {
    static int nodeNum;
    static Edge[][] connected;
    static Node[] node;
    static LinkedList<Node> antPipe;


    public static void main(String args[]) {
        int from, to, percent, special, next, count;
        Scanner in = new Scanner(System.in);
        nodeNum = in.nextInt();
        node = new Node[nodeNum];
        connected = new Edge[nodeNum][nodeNum];
        antPipe = new LinkedList<Node>();
        for (int i = 0; i < nodeNum; i++) {
            node[i] = new Node(0, i);
        }
        in.nextLine();
        for (int i = 0; i < nodeNum - 1; i++) {
            from = in.nextInt() - 1;
            to = in.nextInt() - 1;
            percent = in.nextInt();
            special = in.nextInt();
            node[to].from = node[from];
            Edge newEdge = new Edge(node[from], node[to], percent, special);
            connected[from][to] = newEdge;
            connected[to][from] = newEdge;
            in.nextLine();
        }
        count = 0;
        String line = in.nextLine();
        in = new Scanner(line);
        while (in.hasNext()) {
            if ((next = in.nextInt()) != -1) {
                node[count].min = next;
                antPipe.add(node[count]);
            }
            count++;
        }
        in.close();
        findMin();
        System.out.printf("%.3f \n", node[0].min);
    }

    public static class Node {
        double min;
        Node from;
        int pos;


        public Node(int min, int pos) {
            this.min = min;
            this.pos = pos;
        }
    }

    public static class Edge {
        Node from;
        Node to;
        double percent;
        boolean special = false;


        public Edge(Node from, Node to, int percent, int special) {
            this.from = from;
            this.to = to;
            this.percent = percent * 1.00 / 100;
            this.special = (special == 1) ? true : false;
        }
    }


    public static void findMin() {
        Node from, to;
        double newMin, oldMin;
        double percent;
        boolean special;
        Edge edge;
        Iterator<Node> i = antPipe.listIterator();
        while (i.hasNext()) {
            to = i.next();
            from = to.from;
            while (from != null) {
                edge = connected[to.pos][from.pos];
                if (edge.special) {
                    oldMin = Math.sqrt(to.min);
                    newMin = oldMin / edge.percent;
                } else {
                    newMin = to.min / edge.percent;
                }
                if (newMin > from.min)
                    from.min = newMin;
                to = from;
                from = from.from;
            }
        }
    }
}