/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode curr = dummyHead;
        
        while(l1 != null || l2 != null) {
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;

            // Set up next node if not set up carry number before
            if(curr.next == null) {
                ListNode nextNode = new ListNode(0);
                curr.next = nextNode;
            }
            
            // Set up carry number if need it
            if(curr.next.val + x + y > 9) {
                ListNode temp = new ListNode(1);
                curr.next.next = temp;
            }
            
            curr.next.val = (curr.next.val + x + y) % 10;
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
            curr = curr.next;
        }
        return dummyHead.next;
    }
}