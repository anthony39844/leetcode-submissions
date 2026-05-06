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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        int count = 0;
        a = a - 1;
        ListNode curr1 = list1;
        ListNode curr2 = list1;
        ListNode curr3 = list2;
        while (count != a){
            count++;
            curr1 = curr1.next;
        }
        int count2 = 0;
        while (count2 != b + 1){
            count2++;
            curr2 = curr2.next;
        }
        while(curr3.next != null){
            curr3 = curr3.next;
        }
        curr3.next = curr2;
        curr1.next = list2;
        return list1;
    }
}
