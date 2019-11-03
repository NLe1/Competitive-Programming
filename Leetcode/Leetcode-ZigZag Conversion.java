class Solution {
    public String convert(String s, int numRows) {

        if (numRows == 1) return s;
        String[] table = new String[numRows];
        Arrays.fill(table, "");
        int i = 0;
        int row = 0;
        boolean ascending = true;
        while (i < s.length()) {
            if (ascending && row < numRows - 1) {
                table[row] += s.charAt(i);
                row++;
                i++;
                continue;
            } else if (!ascending && row > 0) {
                table[row] += s.charAt(i);
                row--;
                i++;
                continue;
            } else if (row == 0 || row == numRows - 1) {
                table[row] += s.charAt(i);
                ascending = !ascending;
                i++;
                if (ascending) {
                    row++;
                } else {
                    row--;
                }
                continue;
            }
        }
        String result = "";
        for(int j = 0; j < table.length; j++){
            result += table[j];
        }

        return result;
    }
}