import java.util.*;

public class Anti11 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCase = in.nextInt();
        in.nextLine();
        long start = System.nanoTime();
        ArrayList<Integer> result = new ArrayList<Integer>();
        // base case
        result.add(1);
        result.add(2);
        result.add(3);
        while (testCase > 0) {
            int n = in.nextInt();
            System.out.println(compute(n, result));
            testCase--;
        }
    }


    public static int compute(int n, ArrayList<Integer> result) {
        if (n < result.size()) {
            return result.get(n);
        } else {
            int number = (int) ((2 * compute(n - 1, result) - compute(n - 3, result)) % (1e9 + 7));
            if (number < 0) {
                number += 1e9 + 7;
            }
            result.add(number);
            return result.get(n);
        }
    }
}
