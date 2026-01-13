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
    bool found = false ;
    bool SameTree(TreeNode* a , TreeNode* b){
        if(!a && !b) return true ;
        if(!a || !b || a->val != b->val) return false;
        return SameTree(a->left , b->left) && SameTree(a->right,b->right);
    }
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!root) return found ;
        if(root->val == subRoot->val) found |= SameTree(root,subRoot);
        return isSubtree(root->left,subRoot) || isSubtree(root->right, subRoot) ;
    }
};
