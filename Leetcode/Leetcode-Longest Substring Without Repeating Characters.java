class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()==0)
            return 0;
        int max = 1;
        int count = 1;
        for(int i =0;i< s.length();i++){
            while(checkSeq(s, i, count))
                count++;
            if(count > max)
                max = count;
        }
        return max;
    }
    public static boolean checkSeq(String sq, int stIndex, int length) {
		HashSet<Character> set = new HashSet<>();
		if (stIndex + length + 1 > sq.length())
			return false;
		for (int i = stIndex; i <= stIndex + length; i++) {
			set.add(sq.charAt(i));
		}
		if (length + 1 == set.toArray().length) {
			return true;
		}
		return false;
	}
}