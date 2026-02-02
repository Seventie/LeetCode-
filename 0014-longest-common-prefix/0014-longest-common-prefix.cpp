class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans ="";
        int mini = strs[0].size();
        for(int i =0 ; i < mini ; i ++){
            char n = strs[0][i];
            for(int j =1 ; j <strs.size();j++){
                if(strs[j].size() <= i || strs[j][i] != n) return ans ;
            }
            ans = ans + n;
        }
        return ans ;
    }
};