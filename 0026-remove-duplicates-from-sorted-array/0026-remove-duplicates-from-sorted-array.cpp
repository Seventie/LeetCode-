class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        int size = nums.size();
        int i = 0;
        for(int j = 0 ; j < size ; j++){
            int c = nums[j];
            while((j+1 < size) && (nums[j+1] == c)){
                j++;
            }
            nums[i] = c ;
            i++;
        }
        return i;
    }
};