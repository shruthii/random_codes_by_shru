# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry=0
        sum1=0
        head=None
        curr_node_l1 = l1
        curr_node_l2 = l2
        while curr_node_l1 != None or curr_node_l2 != None:
            if not curr_node_l1 and curr_node_l2:
                curr_node_l1 = ListNode()
            elif not curr_node_l2 and curr_node_l1:
                curr_node_l2 = ListNode()   
            sum1 = curr_node_l1.val + curr_node_l2.val + carry
            if sum1 >=10:
                carry=1
                new_node = ListNode(val=sum1-10)
                if head:
                    trav_node=head
                    while trav_node.next !=None:
                        trav_node=trav_node.next
                    if trav_node.next ==None:
                        trav_node.next = new_node
                    #new_node.next = head
                    #head=new_node
                else:
                    head=new_node
            else:
                new_node = ListNode(val=sum1)
                if head:
                    trav_node=head
                    while trav_node.next !=None:
                        trav_node=trav_node.next
                    if trav_node.next ==None:
                        trav_node.next = new_node
                    #new_node.next = head
                    #head=new_node
                else:
                    head=new_node    
                carry=0
            curr_node_l2=curr_node_l2.next 
            curr_node_l1=curr_node_l1.next
            #head=new_node    
        if carry:
            new_node = ListNode(val=1)
            if head:
                trav_node=head
                while trav_node.next !=None:
                    trav_node=trav_node.next
                if trav_node.next ==None:
                    trav_node.next = new_node
                    #new_node.next = head
                    #head=new_node
        return head       

            ##sum of 2 numbes using single linked list
