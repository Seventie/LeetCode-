class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> store ;
        vector<vector<string>> ans ;
        for(string s : strs){
            string og = s ;
            sort(s.begin(),s.end());
            store[s].push_back(og);
        }
        for (auto &pair : store ) {
            ans.push_back(pair.second);
        }
        return ans ;
    }
};