#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# =============================================================================
"""
@Probelm :   0002.py (Medium)
@First   :   2022/04/15
@URL     :   https://leetcode.com/problems/add-two-numbers/
"""
# =============================================================================

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if self.getLen(l1) < self.getLen(l2):
            l1, l2 = l2, l1
        head = l1
        while l2 is not None:
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next
        # head is not empty here but l1 is empty
        res = head
        while res:
            if res.val > 9:
                res.val -= 10
                if res.next is None:
                    res.next = ListNode(1)
                else:
                    res.next.val += 1
            res = res.next
        return head

    def getLen(self, ls):
        tempLen = 0
        while ls:
            tempLen += 1
            ls = ls.next
        return tempLen

def main():
    s = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = s.addTwoNumbers(l1, l2)
    # [7,0,8]
    while res:
        print(res.val)
        res = res.next

if __name__ == "__main__":
    main()