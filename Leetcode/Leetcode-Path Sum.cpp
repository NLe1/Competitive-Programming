/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode *root, int sum) {
        if(root == nullptr)
            return false;

        if(isLeaf(root) && root -> val == sum)
            return true;

        if(isLeaf(root) && root -> val != sum)
            return false;

        return hasPathSum(root -> left, sum - root -> val) || hasPathSum(root -> right, sum - root -> val);
    }

    bool isLeaf(TreeNode *root){
        return root -> left == NULL && root -> right == NULL;
    }
};