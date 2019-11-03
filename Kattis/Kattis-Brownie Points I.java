import java.util.*;

public class BrowniePoints {
    public static void main(String agrs[]) {
        Scanner in = new Scanner(System.in);
        while (in.hasNextInt()) {
            int t = in.nextInt();
            if (t == 0) {
                break;
            }
            in.nextLine();
            int[][] numPoint = new int[t][2];
            for (int i = 0; i < t; i++) {
                String[] coordinates = in.nextLine().split(" ");
                numPoint[i][0] = Integer.parseInt(coordinates[0].trim());
                numPoint[i][1] = Integer.parseInt(coordinates[1].trim());
            }
            int point1 = 0;
            int point2 = 0;
            int pivot = t / 2;
            for (int i = 0; i < numPoint.length; i++) {
                if ((numPoint[i][0] < numPoint[pivot][0] && numPoint[i][1] > numPoint[pivot][1])
                        || (numPoint[i][0] > numPoint[pivot][0] && numPoint[i][1] < numPoint[pivot][1])) {
                    point1++;
                } else if ((numPoint[i][0] < numPoint[pivot][0] && numPoint[i][1] < numPoint[pivot][1])
                        || (numPoint[i][0] > numPoint[pivot][0] && numPoint[i][1] > numPoint[pivot][1])) {
                    point2++;
                }
            }
            System.out.println(point2 + " " + point1);
        }
    }
}