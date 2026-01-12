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

    bool helper(TreeNode* a , int val){
        if(!a) return true;
        if(a->val != val) return false ;
        return helper(a->left,val) && helper(a->right,val);
    }
    bool isUnivalTree(TreeNode* root) { 
        return helper(root , root->val);
    }
};
