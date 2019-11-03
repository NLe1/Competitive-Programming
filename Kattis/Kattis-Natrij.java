import java.util.*;

public class Natrij {
    public static void main(String args[]) {
        // int counter = 0;
        Scanner in = new Scanner(System.in);
        String start = in.nextLine();
        String end = in.nextLine();

        String[] startString = start.split(":");
        String[] endString = end.split(":");

        int sum1 = 0;
        int sum2 = 0;

        if (Integer.parseInt(endString[0]) <= Integer.parseInt(startString[0])) {
            sum2 += 24 * 3600;
        }

        for (int i = 0; i < startString.length; i++) {
            if (i == 0) {
                sum1 += (Integer.parseInt(startString[i])) * 3600;
                sum2 += (Integer.parseInt(endString[i])) * 3600;
            } else if (i == 1) {
                sum1 += (Integer.parseInt(startString[i])) * 60;
                sum2 += (Integer.parseInt(endString[i])) * 60;
            } else {
                sum1 += (Integer.parseInt(startString[i]));
                sum2 += (Integer.parseInt(endString[i]));
            }
        }

        int subtract = sum2 - sum1;
        int hour = subtract / 3600;
        subtract -= hour * 3600;
        int minute = subtract / 60;
        subtract -= minute * 60;
        int second = subtract;
        System.out.printf("%02d:%02d:%02d", hour, minute, second);
    }
}