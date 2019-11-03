/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> sol = new ArrayList<Integer>();
        TreeNode cur = root;
        TreeNode pre = root;
        while(cur != null){
            if(cur.left == null){
                sol.add(cur.val);
                cur = cur.right;
            }
            else{
                pre = cur.left;
                //get the rightmost child
                while(pre.right != null){
                    pre = pre.right;
                }
                pre.right = cur;
                TreeNode temp = cur;
                cur = cur.left;
                temp.left = null;
            }
        }
        return sol;
    }
}