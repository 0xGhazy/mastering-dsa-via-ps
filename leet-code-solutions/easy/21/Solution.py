from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None:
            return list1
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head1, head2 = list1, list2
        result = ListNode()
        pointer = result

        if list1.val <= list2.val:
            result.val = list1.val
            head1 = head1.next
        else:
            result.val = list2.val
            head2 = head2.next

        
        while head1 != None or head2 != None:
            if head1 != None and head2 != None:
                if head1.val <= head2.val:
                    result.next = ListNode(head1.val)
                    result = result.next
                    head1 = head1.next
                else:
                    result.next = ListNode(head2.val)
                    result = result.next
                    head2 = head2.next
            elif head1 != None:
                result.next = ListNode(head1.val)
                result = result.next
                head1 = head1.next
            elif head2 != None:
                result.next = ListNode(head2.val)
                result = result.next
                head2 = head2.next
        
        return pointer

    def to_array(self, list_: ListNode):
        result = []
        while list_ != None:
            result.append(list_.val)
            list_ = list_.next
        return result




n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n3 = ListNode(4)
n2.next = n3

n_1 = ListNode(1)
n_2 = ListNode(3)
n_1.next = n_2
n_3 = ListNode(4)
n_2.next = n_3


x = Solution()
x.mergeTwoLists(n1, n_1)
