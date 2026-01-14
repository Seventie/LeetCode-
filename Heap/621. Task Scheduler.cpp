// Approach -1 

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freq(26, 0);
        for (char c : tasks) freq[c - 'A']++;

        int maxFreq = 0;
        for (int f : freq) maxFreq = max(maxFreq, f);

        int countMax = 0;
        for (int f : freq)
            if (f == maxFreq) countMax++;

        int slots = (maxFreq - 1) * (n + 1) + countMax;
        return max((int)tasks.size(), slots);
    }
};



// Approach -2 

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> freq;
        for (char c : tasks) freq[c]++;

        // max heap
        priority_queue<int> pq;
        for (auto &x : freq) {
            pq.push(x.second);
        }

        queue<pair<int,int>> cooldown; // {remainingCount, availableTime}
        int time = 0;

        while (!pq.empty() || !cooldown.empty()) {
            time++;

            if (!pq.empty()) {
                int cnt = pq.top();
                pq.pop();
                cnt--;

                if (cnt > 0) {
                    cooldown.push({cnt, time + n});
                }
            }

            if (!cooldown.empty() && cooldown.front().second == time) {
                pq.push(cooldown.front().first);
                cooldown.pop();
            }
        }

        return time;
    }
};
