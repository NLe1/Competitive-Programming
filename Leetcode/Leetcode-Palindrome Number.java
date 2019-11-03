class Solution {
    public boolean isPalindrome(int x) {
       //if x is negative return false
	        if(x < 0) return false;

	        StringBuilder numString = new StringBuilder(Integer.toString(x));

	        if(numString.toString().equals(numString.reverse().toString())){
	            return true;
	        }else{
	            return false;
	        }

    }
}