class Solution {
    public List<String> letterCombinations(String digits) {
        if(digits.length() == 0) {
	        	return new ArrayList<>(0);
	        }
	    	List<String> ctn = new ArrayList<String>();
	        //2->9 to 0->7
	        String[][] map = {
	        		{"a", "b", "c"},
	        		{"d", "e", "f"},
	        		{"g", "h", "i"},
	        		{"j", "k", "l"},
	        		{"m", "n", "o"},
	        		{"p", "q", "r", "s"},
	        		{"t", "u", "v"},
	        		{"w", "x", "y", "z"}};


	        for(int i = 0; i < digits.length(); i++) {
	        	//convert from string to actual indices
	        	int num = Integer.parseInt(digits.charAt(i) + "") - 2 ;
	        	if(i == 0) {
	        		for(int j = 0; j < map[num].length; j++) {
	        			ctn.add(map[num][j]);
	        		}
	        		continue;
	        	}
	        	int size = ctn.size();
	        	for(int a = 0 ; a < size; a++) {
	        		String base = ctn.remove(0);
	        		for(int j = 0; j < map[num].length; j++) {
	        			ctn.add(base + map[num][j]);
	        		}
	        	}
	        }

	        return ctn;
    }
}