class Twitter {
public:
    unordered_map<int, vector<pair<int,int>>> tweets;
    unordered_map<int, unordered_set<int>> followed;
    int time = 0;

    Twitter() {
    }

    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back({time, tweetId});
        time++;
    }

    vector<int> getNewsFeed(int userId) {
        priority_queue<pair<int, int>> pq;
        
        // Add tweets from followed users
        for (auto c : followed[userId]) {
            for (auto s : tweets[c]) {
                pq.push(s);
            }
        }

        // Add tweets from the user themselves
        for (auto c : tweets[userId]) {
            pq.push(c);
        }

        vector<int> tweet;
        // Get the 10 most recent tweets
        for (int i = 0; i < 10; i++) {
            if (pq.empty()) break;
            tweet.push_back(pq.top().second);
            pq.pop();
        }
        return tweet;
    }

    void follow(int followerId, int followeeId) {
        followed[followerId].insert(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        followed[followerId].erase(followeeId);
    }
};
