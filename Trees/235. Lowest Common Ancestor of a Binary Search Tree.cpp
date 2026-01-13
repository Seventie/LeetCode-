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
    queue<TreeNode*> sta ;
    queue<TreeNode*> stb ;
    void helper(TreeNode* r, int a, queue<TreeNode*>& st){
        if(!r) return ;
        while(r->val!= a){
            st.push(r);
            if(r->val > a){
                r = r->left;
            }
            else{
                r = r->right;
            }
        }
        st.push(r);
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        helper(root,p->val,sta);
        helper(root,q->val,stb);
        TreeNode* last = nullptr;
        while(!sta.empty() && !sta.empty() && sta.front()==stb.front()){
            last = sta.front();
            sta.pop();
            stb.pop();
        }
        return last;
    }

};
