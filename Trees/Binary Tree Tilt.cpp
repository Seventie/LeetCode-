class Solution {
public:
    int tilt = 0;

    int dfs(TreeNode* root) {
        if (!root) return 0;

        int leftSum = dfs(root->left);
        int rightSum = dfs(root->right);

        tilt += abs(leftSum - rightSum);

        return root->val + leftSum + rightSum;
    }

    int findTilt(TreeNode* root) {
        dfs(root);
        return tilt;
    }
};
