class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = "";
        int mini = strs[0].size();
        int len = strs.size();
        for(int x = 0 ; x < mini ; x++){
            char now = strs[0][x];
            for(int j = 1 ; j <len ; j++ ){
                if(strs[j].size() <= x || strs[j][x] != now) return ans;
            }
            ans = ans + now ;
        }
        return ans ;
    }
};