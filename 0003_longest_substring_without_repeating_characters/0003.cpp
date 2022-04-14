class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int small = 0;
        int big = 0;
        unordered_map<int, int> mapping;
        int res = 0;
        while (big < s.length()){
            if (mapping.count(s[big])){
                small = max(small, mapping[s[big]]+1);
            }
            mapping[s[big]] = big;
            res = max(res, big - small + 1);
            big ++;
        }
        return res;
    }
};
