class Solution {
public:
    struct compare{
        bool operator()(const vector<int>&p ,vector<int>&q){
            return p[0]*p[0] + p[1]*p[1] > q[0]*q[0] +q[1]*q[1];
        }
    };
    vector<vector<int>> ans;
    priority_queue<vector<int>,vector<vector<int>>, compare> pq;
    void build(vector<int> arr){
        pq.push(arr);
    }
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        for(vector<int> x : points){
            build(x);
        }
        int i = 0;
        while(i != k){
            ans.push_back(pq.top());
            pq.pop();
            i++;
        }
        return ans;
    }
};
