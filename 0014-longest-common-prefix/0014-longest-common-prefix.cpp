class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = "";
        int smallest = strs[0].size() ;
        for(string x : strs){
            if(x.size()<smallest){
                smallest = x.size();
            }
        }
        int i = 0 ;
        while (i < smallest){
            char c = strs[0][i];
            for(string x : strs){
                if(c != x[i]){
                    return ans ;
                }
            }
            ans = ans + c;
            i++;
        }
        return ans ;
    }
};