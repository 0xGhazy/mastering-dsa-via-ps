# URL: https://leetcode.com/problems/palindrome-linked-list/submissions/


# bad solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        myArr = []
        while head:
            myArr.append(head.val)
            head = head.next
            
        if myArr == list(reversed(myArr)):
            return True
        return False