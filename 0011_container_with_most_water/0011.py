#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# =============================================================================
"""
@Probelm :   0011.py (Medium)
@First   :   2022/04/15
@URL     :   https://leetcode.com/problems/container-with-most-water/
"""
# =============================================================================

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==2:
            return min(height)
        left, right = 0, len(height)-1
        res = 0
        while (left < right):
            hgt = min(height[left], height[right])
            newRes = hgt * (right-left)
            if newRes > res:
                res = newRes
            #     resLeft, resRight = left, right
            # res = max(res, newRes)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return res

def main():
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    # 49
    print(sol.maxArea(height))
    height = [1,1]
    # 1
    print(sol.maxArea(height))

if __name__ == "__main__":
    main()
