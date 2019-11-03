class Solution {
    public int firstMissingPositive(int[] nums) {
        HashSet container = new HashSet();

        int max = 0;

        for (int num : nums){
            container.add(num);
            if(num > max){
                max = num;
            }
        }

        for (int i=1 ; i <= max; i++){
            if(!container.contains(i)){
                return i;
            }
        }

        return max + 1;
    }
}