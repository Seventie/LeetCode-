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
    vector<int> test ;
    int helper(TreeNode* a, int val){
        if(!a) return 0;
        int q = 0 ;
        if(a->val >= val){
            q = 1 ;
            val = a->val;
            test.push_back(val);
        }
        return q + helper(a->left,val) + helper(a->right,val);
    }
    int goodNodes(TreeNode* root) {
        int ans = helper(root,INT_MIN);
        for(int x : test){
            cout << x ;
        }
        cout << endl ;
        return ans ;
    }
};
