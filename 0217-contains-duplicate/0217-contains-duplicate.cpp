class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> a ;
        for(int x : nums){
            if(a[x]==1) return true;
            a[x]++;
        }
        return false ;
    }
};