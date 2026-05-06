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
    public boolean isPalindrome(ListNode head) {
        ListNode curr = head;
        int count = 1;
        while(curr.next != null){
            curr = curr.next;
            count++;
        }
        int[] values = new int[count];
        count = 0;
        curr = head;
        while (curr != null){
            values[count] = curr.val;
            count++;
            curr = curr.next;
        }
        for (int i = 0, j = count - 1; i < j; i++, j--){
            if (values[i] != values[j]){
                return false;
            }
        }
        return true;
    }
}
