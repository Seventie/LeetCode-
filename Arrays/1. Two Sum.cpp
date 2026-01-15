class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> st;
        int n = nums.size();
        for(int i =0; i < n ;i++){
            int remain = target - nums[i];
            if(st.count(remain)){
                return {st[remain],i};
            }
            st[nums[i]] = i;
        }
        return {};
    }
};
