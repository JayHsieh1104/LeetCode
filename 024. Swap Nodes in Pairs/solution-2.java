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
        // Deal with base case
        if(head == null || head.next == null) {
            return head;
        }
        ListNode point = head.next;
        head.next = swapPairs(head.next.next);
        point.next = head;
        return point;
    }
}