class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> a ;
        int n = nums.size();
        for(int x : nums){
            a[x]++;
            if(a[x]>n/2) return x;
        }
        return n;    
    }
};
