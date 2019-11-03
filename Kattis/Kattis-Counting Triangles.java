import java.util.*;

public class CountingTriangles {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int numLine = in.nextInt();
        while (numLine != 0) {
            int count = 0;
            double[][] input = new double[numLine][4];
            // reading input
            for (int i = 0; i < numLine; i++) {
                input[i][0] = in.nextDouble();
                input[i][1] = in.nextDouble();
                input[i][2] = in.nextDouble();
                input[i][3] = in.nextDouble();
            }
            for (int i = 0; i < numLine - 2; i++) {
                for (int j = i + 1; j < numLine - 1; j++) {
                    for (int k = j + 1; k < numLine; k++) {
                        if (intersect(input[i], input[j]) && intersect(input[j], input[k])
                                && intersect(input[i], input[k])) {
                            count++;
                        }
                    }
                }
            }
            System.out.println(count);
            numLine = in.nextInt();
        }
        in.close();
    }


    public static boolean intersect(double[] line1, double[] line2) {
        double slope1 = (line1[3] - line1[1]) / (line1[2] - line1[0]);
        double slope2 = (line2[3] - line2[1]) / (line2[2] - line2[0]);
        if (slope1 == slope2)
            return false;
        else {
            double b1 = line1[1] - slope1 * line1[0];
            double b2 = line2[1] - slope2 * line2[0];
            double intersectX = (b2 - b1) / (slope1 - slope2);
            if ((intersectX >= Math.min(line1[0], line1[2]) && intersectX <= Math.max(line1[0], line1[2]))
                    && (intersectX >= Math.min(line2[0], line2[2]) && intersectX <= Math.max(line2[0], line2[2])))
                return true;
            else {
                return false;
            }
        }
    }

}