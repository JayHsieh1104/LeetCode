/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // Deal with corner case
        if(lists.length == 0) {
            return null;
        }
        ListNode dummyHead = new ListNode(0);
        ListNode curr = dummyHead;
        while(true) {
            boolean isBreak = true;  // Used to detect whether go through all the nodes
            int index = 0, min = Integer.MAX_VALUE;
            for(int i = 0; i < lists.length; i++) {
                if(lists[i] == null) {
                    continue;
                }
                else if(lists[i].val < min) {
                    min = lists[i].val;
                    index = i;
                    isBreak = false;
                }
            }
            if(isBreak) {
                break; // All linked list are null, terminate the loop
            }
            curr.next = lists[index];
            curr = curr.next;
            lists[index] = lists[index].next;
        }
        return dummyHead.next;
    }
}