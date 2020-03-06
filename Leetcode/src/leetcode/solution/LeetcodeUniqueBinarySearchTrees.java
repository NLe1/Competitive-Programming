package leetcode.solution;

import java.util.HashMap;

public class LeetcodeUniqueBinarySearchTrees {
    public static int helper(int upper, int lower, HashMap<String, Integer> map){
        String key = String.format("%d_%d", lower, upper);
        if(map.containsKey(key)) return map.get(key);
        if (upper - lower == 0){
            return 1;
        }else if(upper - lower == 1) {
            return 2;
        }else if(upper - lower < 0){
            return 0;
        }
        int numTrees = 0;
        for(int i = lower; i <= upper; i++){
            int left = i > lower ? helper(i - 1, lower, map) : 1;
            int right = i < upper ? helper(upper, i + 1, map) : 1;
            numTrees+=left*right;
        }
        map.put(key, numTrees);
        return numTrees;
    }
    public static int numTrees(int upper) {
        return helper(upper, 1, new HashMap<String, Integer>());
    }
}