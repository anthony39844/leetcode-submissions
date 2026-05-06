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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }
        ListNode curr = head;
        while (curr.next != null){
            if (curr.val == curr.next.val){
                curr.next = curr.next.next;
            }else{
                curr = curr.next;
            }
        }
        // }
        // while (head.val == head.next.val){
        //     head = head.next;
        //     if (head.next == null){
        //         return head;
        //     }
        // }
        // ListNode curr = head;
        // ListNode prev = null;
        // while (curr != null && curr.next != null){
        //     if (curr.val == curr.next.val){
        //         prev.next = curr.next;
        //     }else{
        //         prev = curr;
        //     }
        //     curr = curr.next;
        // }
        return head;
    }
}
