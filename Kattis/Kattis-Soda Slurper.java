import java.util.*;

public class ProblemG {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int emptyBot = in.nextInt();
        int foundBot = in.nextInt();
        emptyBot += foundBot;

        int price = in.nextInt();

        int total = 0;

        while (emptyBot >= price) {
            int boughtBot = emptyBot / price;
            int remainder = emptyBot % price;
            total = total + boughtBot;
            emptyBot = boughtBot + remainder;
        }
        System.out.println(total);
    }
}
