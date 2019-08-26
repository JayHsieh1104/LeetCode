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
        // Use hashset to record each element
        HashSet<ListNode> nodeSet = new HashSet<>();
        // If head == null, the linked list doesn't contain cycle, so terminate the loop 
        while(head != null) {
            if(nodeSet.contains(head)) {
                return true;
            }
            nodeSet.add(head);
            head = head.next;
        }
        return false;
    }
}