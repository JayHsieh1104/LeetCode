/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        // Deal with corner case
        if(head == null || head.next == null) {
            return head;
        }
        
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode prev = dummyHead;
        
        while(head != null) {
            // If only leave one node, terminate the loop
            if(head.next == null) {
                break;
            }
            // Temp is the node behind the two adjacent nodes (P -> F -> S -> Temp)
            ListNode temp = head.next.next;
            // Link the second node to the prev node (P -> S -> Temp)
            prev.next = head.next;
            // Link the first node to the second node (P -> S -> F)
            head.next.next = head;
            // Link temp node to the first node (P -> S -> F -> Temp)
            head.next = temp; 
            // Now, head is on the position of F, so we move head to its next
            head = head.next;
            // Move prev to the next two position
            prev = prev.next.next;        
        }
        return dummyHead.next;
    }
}