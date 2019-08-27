/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Create a dummyHead
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode curr = dummyHead, pivot = curr;
        // Move pivot by n+1 steps from the curr point, to maintain a n+1 constant gap between curr and pivot
        for(int i = 0; i <= n ; i++) {
            pivot = pivot.next;
        }
        // When pivot == null, that means it reaches the end of the linked list
        while(pivot != null) {    
            curr = curr.next;
            pivot = pivot.next;
        }
        // Remove the n-th node from the end of the list
        curr.next = curr.next.next;
        return dummyHead.next;
    }
}