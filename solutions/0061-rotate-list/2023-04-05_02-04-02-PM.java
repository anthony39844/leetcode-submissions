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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0){
            return head;
        }
        ListNode curr = head;
        int count = 0;
        while (curr.next != null){
            curr = curr.next;
            count++;
        }
        if (k != 1 && k % (count + 1) == 0){
            return head;
        }
        if (k > count + 1){
            while ( k > count + 1){
                k = k - (count + 1);
            }
        }
        curr = head;
        for (int i = 0; i < count - k; i++){
            curr = curr.next;
        }
        ListNode lastNode = curr;
        ListNode newHead = curr.next;
        while (curr.next != null){
            curr = curr.next;
        }
        curr.next = head;
        lastNode.next = null;
        head = newHead;
        return head;
    }
}
