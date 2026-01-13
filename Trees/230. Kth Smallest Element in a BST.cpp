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
    vector<int> dfs ;
    void helper(TreeNode* root){
        if(!root) return ;
        helper(root->left);
        dfs.push_back(root->val);
        helper(root->right);
    }
    int kthSmallest(TreeNode* root, int k) {
        helper(root);
        return dfs[k-1];
    }
};
