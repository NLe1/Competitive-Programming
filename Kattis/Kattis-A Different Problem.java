import java.util.*;

public class ADifferentProblem {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String line;
        String[] num;
        long num1, num2;
        while (in.hasNextLine()) {
            line = in.nextLine();
            if (line.equals(""))
                break;
            num = line.split(" ");
            num1 = Long.parseLong(num[0]);
            num2 = Long.parseLong(num[1]);
            System.out.println(Math.abs(num1 - num2));
        }
        in.close();
    }
}