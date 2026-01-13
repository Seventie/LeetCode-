/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(!root) return new TreeNode(val);
        TreeNode* iter = root ;
        while(iter){
            if(!iter->left && !iter->right) {
                if(iter->val> val){
                    iter->left = new TreeNode(val);
                    return root;
                }
                else{
                    iter->right = new TreeNode(val);
                    return root;
                }
            }
            else if(!iter->left && iter->val >val){
                iter->left = new TreeNode(val);
                return root;
            }
            else if(!iter->right && iter->val < val){
                iter->right = new TreeNode(val);
                return root;
            }
            else{ 
            if(iter->val> val){
                iter = iter->left;
            }
            else{
                iter = iter->right;
            }}
        }
        return root;
    }
};
