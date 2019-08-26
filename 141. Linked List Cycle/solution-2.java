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
    public boolean hasCycle(ListNode head) {
        // Deal with corner case
        if(head == null || head.next == null) {
            return false;
        }    
        ListNode fast = head.next;
        while(fast != head) {
            // Reach the end of the linked list
            if(fast == null || fast.next == null) {
                return false;
            }
            fast = fast.next.next;
            head = head.next;
        }
        return true;
    }
}