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
    bool isEvenOddTree(TreeNode* root) {
        if (!root) return true;

        queue<TreeNode*> q;
        q.push(root);

        bool level = 0; 

        while (!q.empty()) {
            int n = q.size();
            int prev = level ? INT_MAX : INT_MIN;

            while (n--) {
                TreeNode* curr = q.front();
                q.pop();

                if (!level && curr->val % 2 == 0) return false;
                if (level && curr->val % 2 == 1) return false;

                if (!level) { 
                    if (curr->val <= prev) return false;
                } else {   
                    if (curr->val >= prev) return false;
                }

                prev = curr->val;

                if (curr->left) q.push(curr->left);
                if (curr->right) q.push(curr->right);
            }

            level ^= 1;
        }

        return true;
    }
};
