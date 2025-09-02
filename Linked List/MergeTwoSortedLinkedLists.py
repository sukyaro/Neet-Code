from typing import Optional

# The test is written by Chat-GPT to be able to test the program myself the way neet code does it
# Definition for singly-linked list (LeetCode provides this automatically).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Checking that none of the lists is empty
        if list1 is None and list2 is None: # if both are empty returning None
            return None
        elif list1 is None: # If the fist one is empty returning the second one
            return list2
        elif list2 is None: # if the second list is empty returning the first one
            return list1
        
        # Setting the 2 lists and the head for the new list
        curr = list1
        curr2 = list2
        if curr.val <= curr2.val:
            newLinkedList = ListNode(curr.val)
            curr = curr.next
        else:
            newLinkedList = ListNode(curr2.val)
            curr2 = curr2.next
            
        newCurr = newLinkedList

        # Going through the lists and adding the smaller elements from each of them
        while curr and curr2:
            if curr.val <= curr2.val:
                newCurr.next = ListNode(curr.val)
                newCurr = newCurr.next
                curr = curr.next
            else:
                newCurr.next = ListNode(curr2.val)
                newCurr = newCurr.next
                curr2 = curr2.next
        
        # Dealing with leftovers
        while curr:
            newCurr.next = ListNode(curr.val)
            newCurr = newCurr.next
            curr = curr.next
        
        while curr2:
            newCurr.next = ListNode(curr2.val)
            newCurr = newCurr.next
            curr2 = curr2.next
                
        # Returning the new list
        return newLinkedList
        
            


# Helper: build a linked list from a Python list.
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

# Helper: convert a linked list back to a Python list.
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# A little test of the program
if __name__ == "__main__":
    # Example input
    input_list1 = [1, 2, 4]
    input_list2 = [1, 3, 5]
    
    # Convert input list -> linked list
    head1 = build_linked_list(input_list1)
    head2 = build_linked_list(input_list2)
    
    # Run your solution
    solution = Solution()
    reversed_head1 = solution.mergeTwoLists(head1, head2)
    
    # Convert output linked list -> Python list
    output_list1 = linked_list_to_list(reversed_head1)
    
    print("Input:", input_list1)
    print("Output:", output_list1)