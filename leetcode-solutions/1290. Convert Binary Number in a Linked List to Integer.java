// URL: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public int getDecimalValue(ListNode head) {
        StringBuilder binaryString = new StringBuilder("");
        while(head != null){
            binaryString.append(head.val);
            head = head.next;
        }
        int x = Integer.parseInt(binaryString.toString(), 2);
        return x;
    }
}