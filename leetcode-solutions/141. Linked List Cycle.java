/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head){
        // check if the LinkedList is empty.
        if (head == null) {
    	    return false;
        }

        // Fast is always ahead of the slow pointer
        ListNode slow = head;
        ListNode fast = head.next;
        

        // loop over the list untill they meet again or reach the end.
        while(fast != slow){
            // check if fast reach the end of the list
            if(fast == null || fast.next == null){
                return false;
            }
            // increment the 2 pointers
            slow = slow.next;
            fast = fast.next.next;
        }
        return true;
    }
}