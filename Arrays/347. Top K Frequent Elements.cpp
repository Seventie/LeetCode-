class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int,int>> pq;
        unordered_map<int,int> st ;
        for(int x: nums) st[x]++ ;
        for (auto &p : st) {
            pq.push({p.second,p.first});
        }
        vector<int> ans ;
        while(k--){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        return ans;
    }
};
