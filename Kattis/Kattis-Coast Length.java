import java.util.*;

public class CoastLength {
    static int m, n;
    static int[][] map; // store the map
    static int count = 0;
    static boolean visited[][];


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        m = in.nextInt() + 2;
        n = in.nextInt() + 2;
        map = new int[m][n]; // make the outside border bigger by 2 size
        visited = new boolean[m][n];
        in.nextLine();
        String[] lineSplit;
        for (int i = 1; i < m - 1; i++) {
            lineSplit = in.nextLine().split("");
            for (int j = 0; j < lineSplit.length; j++) {
                map[i][j + 1] = Integer.parseInt(lineSplit[j]);
            }
        }
        traverse(0, 0);
        System.out.println(count);
    }


    public static void traverse(int i, int j) {
        if (i < 0 || j < 0 || i > m - 1 || j > n - 1 || visited[i][j]) {
            return;
        }
        if (map[i][j] == 1) {
            count++;
            return;
        }
        visited[i][j] = true;
        traverse(i + 1, j);
        traverse(i - 1, j);
        traverse(i, j + 1);
        traverse(i, j - 1);
    }


    public static void printMap(int[][] map) {
        for (int i = 0; i < m; i++) {
            System.out.println(Arrays.toString(map[i]));
        }
    }

}
