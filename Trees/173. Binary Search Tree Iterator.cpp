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
class BSTIterator {
public:
    queue<int> nodes;
    void bfs(TreeNode* a){
        if(!a) return ;
        bfs(a->left);
        nodes.push(a->val);
        bfs(a->right);
    }
    BSTIterator(TreeNode* root) {
        bfs(root);
    }
    int next() {
        int ans = nodes.front();
        nodes.pop();
        return ans ;
    }
    
    bool hasNext() {
        if(!nodes.empty()) return true ;
        return false ;
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
