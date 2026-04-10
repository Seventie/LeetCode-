class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n,1);
        vector<int> a(n,1);
        vector<int> a(n,1);
        int p = 1 ;
        for(int x =0 ;x <n ; x++){
            p = a[x]* p;
            a[x] = p;
        }
        int p = 1 ;
        for(int x =n-1 ;x >=0 ; x--){
            p = a[x]* p;
            a[x] = p;
        }
        for(int i =0 ; i < n ; i++){
            if(i==0){
                ans[i] =b[i+1];
            }
            else if(i == n-1){
                ans[i] = a[i-1];
            }
            else{
                ans[i] = a[i-1] * b[i+1];
            }
        }
        return ans ;
    }
};
1,2,6,24
24,24,12,4