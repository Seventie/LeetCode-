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
    bool isCousins(TreeNode* root, int x, int y) {
        if (!root) return false;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int n = q.size();
            bool found_x = false;
            bool found_y = false;
            int parent_x = -1, parent_y = -1;

            while (n--) {
                TreeNode* curr = q.front();
                q.pop();

                // sibling check
                if (curr->left && curr->right) {
                    if ((curr->left->val == x && curr->right->val == y) ||
                        (curr->left->val == y && curr->right->val == x)) {
                        return false;
                    }
                }

                if (curr->left) {
                    if (curr->left->val == x) {
                        found_x = true;
                        parent_x = curr->val;
                    } else if (curr->left->val == y) {
                        found_y = true;
                        parent_y = curr->val;
                    }
                    q.push(curr->left);
                }

                if (curr->right) {
                    if (curr->right->val == x) {
                        found_x = true;
                        parent_x = curr->val;
                    } else if (curr->right->val == y) {
                        found_y = true;
                        parent_y = curr->val;
                    }
                    q.push(curr->right);
                }
            }

            if (found_x && found_y)
                return parent_x != parent_y;

            if (found_x || found_y)
                return false;
        }

        return false;
    }
};
