#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# =============================================================================
"""
@Probelm :   0005.py (Medium)
@First   :   2022/04/15
@URL     :   https://leetcode.com/problems/longest-palindromic-substring/submissions/
"""
# =============================================================================

class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLen = len(s)
        left = 0
        maxLen = 1
        dp = [[0] * (strLen) for i in range(strLen)]
        for i in range(strLen):
            dp[i][i] = 1
            for j in range(i):
                # dp equation
                if (s[i] == s[j]) and ((i-j<2) or (dp[j+1][i-1])):
                    dp[j][i] = 1
                    if maxLen < i-j+1:
                        left = j
                        maxLen = i-j+1
        return s[left:left+maxLen]

def main():
    s = Solution()
    ss = "babad"
    # "bab"
    print(s.longestPalindrome(ss))

if __name__ == "__main__":
    main()