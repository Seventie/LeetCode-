class Solution {
public:
    string reorganizeString(string s) {
        unordered_map<char,int> freq;
        for (char c : s) freq[c]++;
        priority_queue<pair<int,char>> pq;
        for (auto &x : freq) {
            pq.push({x.second, x.first});
        }
        string ans = "";
        pair<int,char> prev = {0, '#'};
        while (!pq.empty()) {
            auto [cnt, ch] = pq.top();
            pq.pop();
            ans.push_back(ch);
            cnt--;
            if (prev.first > 0) {
                pq.push(prev);
            }
            prev = {cnt, ch};
        }
        if (ans.size() != s.size()) return "";
        return ans;
    }
};
