from typing import Optional

# The test is written by Chat-GPT to be able to test the program myself the way neet code does it
# Definition for singly-linked list (LeetCode provides this automatically).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # Creating a new linked list 
        curr = head
        
        # Going through the entire linked list
        while curr: 
            next = curr.next # saving the pointer to the next element
            curr.next = prev # reversing the pointer of the current element to the previous one
            prev = curr # now previous becomes current
            curr = next # and moving along the linked list
        
        # Returning the new linked list
        return prev
            


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
    input_list1 = [0, 1, 2, 3]
    input_list2 = []
    
    # Convert input list -> linked list
    head1 = build_linked_list(input_list1)
    head2 = build_linked_list(input_list2)
    
    # Run your solution
    solution = Solution()
    reversed_head1 = solution.reverseList(head1)
    reversed_head2 = solution.reverseList(head2)
    
    # Convert output linked list -> Python list
    output_list1 = linked_list_to_list(reversed_head1)
    output_list2 = linked_list_to_list(reversed_head2)
    
    print("Input:", input_list1)
    print("Output:", output_list1)
    print()
    print("Input:", input_list2)
    print("Output:", output_list2)