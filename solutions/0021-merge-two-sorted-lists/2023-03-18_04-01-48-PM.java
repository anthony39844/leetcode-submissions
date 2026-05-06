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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Create a dummy node as the head of the merged list
        ListNode dummy = new ListNode(0);
        // Create a pointer to the current node of the merged list
        ListNode current = dummy;
        // Traverse both lists until one of them ends
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                // Add the current node of list1 to the merged list
                current.next = list1;
                // Move the pointer of list1 to the next node
                list1 = list1.next;
            } else {
                // Add the current node of list2 to the merged list
                current.next = list2;
                // Move the pointer of list2 to the next node
                list2 = list2.next;
            }
            // Move the pointer of the merged list to the newly added node
            current = current.next;
        }
        
        // Append the remaining nodes of the non-empty list to the merged list
        if (list1 != null) {
            current.next = list1;
        } else {
            current.next = list2;
        }
        
        // Return the head of the merged list, which is the next node of the dummy node
        return dummy.next;
    }
}
