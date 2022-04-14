#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# =============================================================================
"""
@Probelm :   0001.py (Easy)
@First   :   2022/04/15
@URL     :   https://leetcode.com/problems/two-sum/
"""
# =============================================================================

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in mapping:
                return [index, mapping[diff]]
            mapping[value] = index


def main():
    nums = [2,7,11,15]
    target = 9
    s = Solution()
    # [0,1]
    print(s.twoSum(nums, target))

if __name__ == "__main__":
    main()