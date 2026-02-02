class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> store;
        for (int i = 0; i < nums.size(); i++) {
            int left = target - nums[i];
            if (store.find(left) != store.end()) {
                return {store[left], i};
            }
            store[nums[i]] = i;
        }
        return {};
    }
};
