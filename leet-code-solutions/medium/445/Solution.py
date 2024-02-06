from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1, number2 = "", ""
        while l1 != None:
            number1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            number2 += str(l2.val)
            l2 = l2.next
        result = str(int(number1) + int(number2))
        result_head = ListNode(result[0])
        head = result_head
        for i in range(1, len(result)):
            result_head.next = ListNode(int(result[i]))
            result_head = result_head.next
        return head
        # print the list
        # while head != None:
        #     print(head.val)
        #     # number2 += str(result_head.val)
        #     head = head.next


n1 = ListNode(5)
n2 = ListNode(6)
n3 = ListNode(4)
n1.next = n2
n2.next = n3

n_1 = ListNode(7)
n_2 = ListNode(2)
n_3 = ListNode(4)
n_4 = ListNode(3)
n_1.next = n_2
n_2.next = n_3
n_3.next = n_4


x = Solution()
x.addTwoNumbers(n_1, n1)
        