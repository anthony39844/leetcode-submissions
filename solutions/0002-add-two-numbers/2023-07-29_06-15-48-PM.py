# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        #reverse both numbers
        head1 = l1
        head2 = l2
        prev1 = None
        prev2 = None
        while head1:
            next1 = head1.next
            head1.next = prev1
            prev1 = head1
            head1 = next1
        
        while head2:
            next2 = head2.next
            head2.next = prev2
            prev2 = head2
            head2 = next2
        #prev1 and prev2 are the heads of the reversed numbers

        one = prev1
        two = prev2
        #turn them into lists
        while one:
            list1.append(one.val)
            one = one.next

        while two:
            list2.append(two.val)
            two = two.next

        #turn them into numbers
        num1 = int(''.join(map(str, list1)))
        num2 = int(''.join(map(str, list2)))
        summ = num1 + num2

        #if the sum is 0 then just return 0
        if summ == 0:
            return ListNode(0)

        sumlist = []

        #now turn the sum back into a list, this will also reverse it
        while summ / 10 != 0:
            sumlist.append(summ % 10)
            summ = summ // 10
        
        answer = ListNode(None)
        curr = answer

        #turn that list into a linkedlist
        for i in range(len(sumlist)):
            curr.next = ListNode(sumlist[i])
            curr = curr.next

        return answer.next
