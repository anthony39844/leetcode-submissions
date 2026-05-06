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
    public ListNode detectCycle(ListNode head) {
        ArrayList<ListNode> already = new ArrayList<ListNode>();
        ListNode curr = head;
        while (curr != null){
            if (already.contains(curr)){
                return curr;
            }else{
                already.add(curr);
            }
            curr = curr.next;
        }
        return null;
    }
}
