#Completed August 11, 2025

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #current node initialization
        currNodeL1 = l1
        currNodeL2 = l2

        #Empty string initialization
        strL1 = ""
        strL2 = ""

        #stringify the nodes in the first list
        while(currNodeL1):
            strL1 += str(currNodeL1.val)
            currNodeL1 = currNodeL1.next
            
        #stringify the nodes in the second list
        while(currNodeL2):
            strL2 += str(currNodeL2.val)
            currNodeL2 = currNodeL2.next
        
        #reverse the strings and turn them into integers
        intL1 = int(strL1[::-1])
        intL2 = int(strL2[::-1])

        #add the integers
        ans = intL1 + intL2

        #stringify the int answer and reverse it
        strL3 = str(ans)[::-1]

        #create a new linked list
        head = ListNode(0)
        currNodeL3 = head
        for i in range(len(strL3)):
            currNodeL3.next = ListNode(int(strL3[i]))
            currNodeL3 = currNodeL3.next
            
        return head.next
        