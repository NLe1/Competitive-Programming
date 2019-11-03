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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if(!root)return {};
        vector<int> num;
        vector<vector<int>> r;
        traverseAndSave(root, &r, num, sum);

        return r;
    }

    void traverseAndSave(TreeNode *root, vector<vector<int>>* r, vector<int> num, int sum){
        num.push_back(root -> val);

        //check if it is leaves node
        if(root -> left == NULL && root -> right == NULL){
            //get the sum of the path
            int total = 0;
            for (int i = 0;i < num.size();i++){
                total += num[i];
            }

            if(total == sum){
                r->push_back(num);
                num.pop_back();
                return;
            }
            else {
                //get rid of the last element and return
                num.pop_back();
                return;
            }
        }

        if(root -> left != NULL)
            traverseAndSave(root -> left,r, num, sum);

        if(root -> right != NULL)
            traverseAndSave(root -> right,r, num, sum);

        num.pop_back();
    }
};