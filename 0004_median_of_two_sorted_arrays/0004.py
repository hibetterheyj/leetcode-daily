#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# =============================================================================
"""
@Probelm :   0004.py (Hard)
@First   :   2022/04/14
@URL     :   https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
# =============================================================================
from heapq import *
from typing import List

class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = [] # store in minus format

    def insert2heap(self, val):
        # print("before:", self.minHeap, self.maxHeap)
        if len(self.maxHeap) == 0:
            heappush(self.minHeap, val)
        else:
            if val < -self.maxHeap[0]:
                heappush(self.minHeap, -heappop(self.maxHeap))
                heappush(self.maxHeap, -val)
            else:
                heappush(self.minHeap, val)
        # print("mid:", self.minHeap, self.maxHeap)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            heappush(self.maxHeap, -heappop(self.minHeap))
        # print("after:", self.minHeap, self.maxHeap)

    def findMid(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (heappop(self.minHeap) - heappop(self.maxHeap))/2.0
        else:
            return heappop(self.minHeap)/1.0

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums1:
            self.insert2heap(num)
        for num in nums2:
            self.insert2heap(num)
        return self.findMid()

def main():
    s = Solution()
    nums1 = [2, 3]
    nums2 = [1]
    print(s.findMedianSortedArrays(nums1, nums2))

if __name__ == "__main__":
    main()