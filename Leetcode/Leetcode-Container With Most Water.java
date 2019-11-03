class Solution {
    public int maxArea(int[] height) {

        //if n = 2 the max is the only result
        if(height.length == 2){
            return (int) Math.pow(Math.min(height[0], height[1]),2);
        }

        int maxArea = 0;
        int varArea = 0;

        for(int i = 0; i < height.length; i++){
            for (int j = 1; j < height.length; j++){
                if(j != i){
                    varArea = (int) (Math.min(height[i], height[j]) * Math.abs(i-j));
                    maxArea = (varArea > maxArea) ? varArea : maxArea;
                }
            }
        }

        return maxArea;
    }
}