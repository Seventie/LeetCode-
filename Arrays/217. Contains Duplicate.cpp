class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> a;
        for(int i : nums){
            a[i]++;
            if(a[i]>1) return true ;
        }
        return false;
    }
};
