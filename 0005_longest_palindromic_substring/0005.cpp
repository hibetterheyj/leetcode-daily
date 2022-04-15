class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        else {
            int left = 0;
            int maxLen = 1;
            int strLen = s.size();
            int dp[strLen][strLen];
            // memset(dp, 0, sizeof(dp));
            for (int i=0; i<strLen; i++){
                dp[i][i]=1;
                for (int j=0; j<i; j++){
                    dp[j][i] = (s[i]==s[j]) && (i-j<2 || dp[j+1][i-1]);
                    if (dp[j][i]==1 && maxLen<i-j+1) {
                        maxLen = i-j+1;
                        left = j;
                    }
                }
            }
            return s.substr(left, maxLen);
        }
    }
};
