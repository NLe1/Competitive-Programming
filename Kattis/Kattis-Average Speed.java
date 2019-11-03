import java.util.*;

public class ProblemF {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double distance = 0;
        int speed = 0;
        int startSecond = 1;
        int endSecond = 0;
        while (in.hasNextLine()) {
            String line = in.nextLine();
            String[] lineSplit = line.split(" ");
            if (lineSplit.length == 2) {
                String[] time = lineSplit[0].split(":");
                int minus = startSecond;
                startSecond = 0;
                startSecond += Integer.parseInt(time[0]) * 3600;
                startSecond += Integer.parseInt(time[1]) * 60;
                startSecond += (Integer.parseInt(time[2]));
                distance += ((startSecond - minus) * 1.00 / 3600) * speed;
                speed = Integer.parseInt(lineSplit[1]);
            } else {
                String[] time = lineSplit[0].split(":");
                endSecond += Integer.parseInt(time[0]) * 3600;
                endSecond += Integer.parseInt(time[1]) * 60;
                endSecond += (Integer.parseInt(time[2]));
                int totalTime = endSecond - startSecond;
                distance += (totalTime * 1.00 / 3600) * speed;
                startSecond = endSecond;
                endSecond = 0;
                System.out.printf("%s %.02f km \n", lineSplit[0], distance);
            }
        }
    }
}