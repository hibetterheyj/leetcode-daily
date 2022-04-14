#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# =============================================================================
"""
@Probelm :   0003.py (Medium)
@First   :   2022/04/15
@URL     :   https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
# =============================================================================

# from heapq import *
# from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        small, big = 0, 0
        res = 0
        char = dict()
        while big < len(s):
            if s[big] in char:
                # find the next position of the same char
                small = max(small, char[s[big]]+1)
            # update char-index mapping
            char[s[big]] = big
            # update result
            res = max(res, big-small+1)
            big += 1
        return res


def main():
    s = Solution()
    ss = "pwwkew"
    # 3
    print(s.lengthOfLongestSubstring(ss))

if __name__ == "__main__":
    main()