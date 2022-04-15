#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# =============================================================================
"""
@Probelm :   001o.py (Hard)
@First   :   2022/04/15
@URL     :   https://leetcode.com/problems/regular-expression-matching/
"""
# =============================================================================

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # corner cases
        if s==p:
            return True
        m, n = len(s), len(p)
        dp = [[0]*(n+1) for _ in range(m+1)]
        # base cases
        dp[0][0] = 1
        # dp[0][nonzero] corner cases: s='' p='a*b*'
        for j in range(1, n):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1]
        for i in range(m):
            for j in range(n):
                if p[j]==s[i] or p[j]=='.':
                    dp[i+1][j+1] = dp[i][j]
                if p[j]=='*':
                    # print('Compare s={} p={}'.format(s[:i+1], p[:j+1]))
                    # print('dp[{}][{}]={}'.format(i+1, j-1, dp[i+1][j-1]))
                    dp[i+1][j+1] = dp[i+1][j-1]
                    if p[j-1]==s[i] or p[j-1]=='.':
                        # consider both cases
                        dp[i+1][j+1] = dp[i+1][j+1] or dp[i][j+1]
                    # print('dp[{}][{}]={}'.format(i+1, j+1, dp[i+1][j+1]))
        # print(dp)
        return dp[m][n]


def main():
    sol = Solution()
    s = "aa"; p = "a"
    # false
    print(sol.isMatch(s, p))
    s = "ab"; p = ".*"
    # true
    print(sol.isMatch(s, p))
    s = ""; p = "b"
    # false
    print(sol.isMatch(s, p))
    s = "aaa"; p = "ab*a*c*a"
    # true
    print(sol.isMatch(s, p))

if __name__ == "__main__":
    main()