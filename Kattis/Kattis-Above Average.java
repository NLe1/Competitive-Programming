import java.util.*;

public class AboveAverage {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int testCase = in.nextInt();
        while (testCase > 0) {
            int totalScore = 0;
            int numStudent = in.nextInt();
            int[] studentScore = new int[numStudent];
            for (int j = 0; j < numStudent; j++) {
                int score = in.nextInt();
                studentScore[j] = score;
                totalScore += score;
            }
            int aboveAverage = 0;
            double averageScore = totalScore / numStudent;
            for (int k = 0; k < studentScore.length; k++) {
                if (studentScore[k] > averageScore) {
                    aboveAverage++;
                }
            }
            float percentage = ((float) aboveAverage) / numStudent * 100;
            System.out.println();
            System.out.printf("%.3f", percentage);
            System.out.print("%");
            testCase--;
        }
    }
}
