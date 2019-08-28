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
        // Define comparator for priority queue
        Comparator<ListNode> cmp;
        cmp = new Comparator<ListNode>() {
        @Override
        public int compare(ListNode o1, ListNode o2) {
            return o1.val - o2.val;
        }    
        };
        // Add every head of every linked list into priority queue.
        Queue<ListNode> q = new PriorityQueue<ListNode>(cmp);
        for(ListNode l : lists) {
            if(l != null) {
                q.add(l);
            }
        }
        // Pop the smallest element from the queue and add it to the final linked list
        ListNode head = new ListNode(0);
        ListNode point = head;
        while(!q.isEmpty()) {
            point.next = q.poll();
            point = point.next;
            // Add the next element into the queue if it's not null
            ListNode next = point.next;
            if(next!=null){
                q.add(next);
            }
        }
        return head.next;
    }
}