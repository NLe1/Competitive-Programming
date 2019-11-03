import java.util.*;

public class ProblemD {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int testCase = in.nextInt();
        while (testCase > 0) {
            int firstDegree = in.nextInt();
            int[] firstCoef = new int[firstDegree + 1];
            for (int i = 0; i < firstCoef.length; i++) {
                firstCoef[i] = in.nextInt();
            }
            int secondDegree = in.nextInt();
            int[] secondCoef = new int[secondDegree + 1];
            for (int i = 0; i < secondCoef.length; i++) {
                secondCoef[i] = in.nextInt();
            }
            int[] totalDegree = new int[firstDegree + secondDegree + 1];
            for (int i = 0; i < firstCoef.length; i++) {
                for (int j = 0; j < secondCoef.length; j++) {
                    totalDegree[i + j] += (firstCoef[i] * secondCoef[j]);
                }
            }
            System.out.println(totalDegree.length - 1);
            for (int i = 0; i < totalDegree.length; i++) {
                System.out.print(totalDegree[i] + " ");
            }
            testCase--;
        }
    }
}
