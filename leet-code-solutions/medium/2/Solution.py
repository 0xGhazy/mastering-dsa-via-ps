from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return ListNode()
        
        number1, number2 = "", ""
        f_head = l1
        while f_head != None:
            number1 += str(f_head.val)
            f_head = f_head.next
        number1 = number1[::-1]

        s_head = l2
        while s_head != None:
            number2 += str(s_head.val)
            s_head = s_head.next
        number2 = number2[::-1]

        result = str(int(number1) + int(number2))[::-1]
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

            

        


n1 = ListNode(2)
n2 = ListNode(4)
n1.next = n2
n3 = ListNode(9)
n2.next = n3

n_1 = ListNode(5)
n_2 = ListNode(6)
n_1.next = n_2
n_3 = ListNode(4)
n_2.next = n_3
n_4 = ListNode(9)
n_3.next = n_4

s = Solution()
print(s.addTwoNumbers(n1, n_1))


# [7,0,4,0,1]
