import java.util.*;

public class CountingStars {
    static char[][] map;
    static boolean[][] visited;
    static int mapW, mapH;
    static int count = 0;


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuilder s = new StringBuilder();
        int ans = 0;
        while (in.hasNextLine()) {
            String line = in.nextLine();
            if (line.equals(""))
                break;
            count++;
            mapH = Integer.parseInt(line.split(" ")[0]);
            mapW = Integer.parseInt(line.split(" ")[1]);
            map = new char[mapH][mapW];
            visited = new boolean[mapH][mapW];
            for (int i = 0; i < mapH; i++)
                map[i] = in.nextLine().toCharArray();
            for (int i = 0; i < mapH; i++) {
                for (int j = 0; j < mapW; j++) {
                    if (!visited[i][j] && map[i][j] == '-') {
                        connectedComponent(i, j);
                        ans++;
                    }
                }
            }
            s.append("Case " + count + ": " + ans + "\n");
            ans = 0;
        }
        System.out.print(s.toString());

        in.close();

    }


    private static void connectedComponent(int i, int j) {
        if (i < 0 || j < 0 || i > mapH - 1 || j > mapW - 1 || visited[i][j] || map[i][j] != '-')
            return;
        visited[i][j] = true;
        connectedComponent(i, j - 1);
        connectedComponent(i, j + 1);
        connectedComponent(i - 1, j);
        connectedComponent(i + 1, j);
    }
}