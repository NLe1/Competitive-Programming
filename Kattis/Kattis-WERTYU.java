import java.util.*;

public class WERTYU {
    public static void main(String args[]) {
        HashMap<String, String> map = new HashMap<String, String>();
        String[][] key = { { "\"", "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=" },
                { "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\" },
                { "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "\'" },
                { "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/" } };
        for (int i = 0; i < key.length; i++) {
            for (int j = 1; j < key[i].length; j++) {
                map.put(key[i][j], key[i][j - 1]);
            }
        }
        Scanner in = new Scanner(System.in).useDelimiter("");
        StringBuilder sb = new StringBuilder();
        while (in.hasNextLine()) {
            String line = in.nextLine();
            if (line.equals(""))
                break;
            String[] character = line.split("");
            for (int i = 0; i < character.length; i++) {
                if (character[i].equals(" ")) {
                    sb.append(" ");
                } else {
                    sb.append(map.get(character[i]));
                }
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }
}