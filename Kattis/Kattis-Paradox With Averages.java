import java.util.*;

public class ProblemB {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        int timeCase = in.nextInt();
        ArrayList<Integer> result = new ArrayList<Integer>();
        while (timeCase > 0) {
            int count = 0;
            int totalCsEq = 0;
            int totalEEq = 0;
            int csStudent = in.nextInt();
            int eStudent = in.nextInt();
            int[] csSmart = new int[csStudent];
            int[] eSmart = new int[eStudent];
            for (int i = 0; i < csSmart.length; i++) {
                csSmart[i] = in.nextInt();
                totalCsEq += csSmart[i];
            }
            for (int i = 0; i < eSmart.length; i++) {
                eSmart[i] = in.nextInt();
                totalEEq += eSmart[i];
            }

            double averageCsSmart = totalCsEq * 1.00 / csStudent;
            double averageESmart = totalEEq * 1.00 / eStudent;
            for (int i = 0; i < csStudent; i++) {
                if (csSmart[i] < averageCsSmart && csSmart[i] > averageESmart)
                    count++;
            }
            result.add(count);
            timeCase--;
        }
        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }
}