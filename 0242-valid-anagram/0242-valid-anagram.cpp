class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size()!=t.size()) return false ;
        vector<int> store(26);
        for (char x : s ){
            int index = x - 'a';
            store[index]++ ;
        }
        for (char x : t){
            int index = x - 'a';
            if (store[index]<=0) return false ;
            store[index]--;
        }
        return true ;
    }
};