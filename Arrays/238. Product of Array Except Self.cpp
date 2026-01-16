class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> a(n, 1), b(n, 1), ans(n, 1);
        int m = 1;
        for(int i = 0; i < n; i++){
            m *= nums[i];
            a[i] = m;
        }

        m = 1;
        for(int i = n - 1; i >= 0; i--){
            m *= nums[i];
            b[i] = m;
        }
        for(int i = 0; i < n; i++){
            if(i == 0)
                ans[i] = b[i + 1];
            else if(i == n - 1)
                ans[i] = a[i - 1];
            else
                ans[i] = a[i - 1] * b[i + 1];
        }
        return ans;
    }
};
