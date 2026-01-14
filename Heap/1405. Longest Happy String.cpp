class Solution {
public:
    string ans ;
    string longestDiverseString(int a, int b, int c) {
        priority_queue<pair<int,char>> pq;
        if(a>0) pq.push({a,'a'});
        if(b>0) pq.push({b,'b'});
        if(c>0) pq.push({c,'c'});
        string prev = "##";
        while(!pq.empty()){
            char cur = pq.top().second;
            int val  = pq.top().first;
            pq.pop();
            if(prev == string(2, cur)){
                if(pq.empty()) return ans;
                char cur1 = pq.top().second;
                int val1  = pq.top().first;
                pq.pop();
                pq.push({val,cur});
                cur = cur1;
                val = val1;
            }
            ans = ans + cur ;
            if(cur == 'a') a--;
            if(cur=='b') b--;
            if(cur=='c') c--;
            swap(prev[0],prev[1]);
            prev[1]=cur;
            val --;
            if(val>0) pq.push({val,cur});
        }
        return ans;
    }
};
