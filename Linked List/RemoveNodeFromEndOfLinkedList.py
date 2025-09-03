
from typing import Optional

# The test is written by Chat-GPT to be able to test the program myself the way neet code does it
# Definition for singly-linked list (LeetCode provides this automatically).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Find the length of the linked list
        listLen = 1
        tail = head
        while tail.next:            # traverse until the last node
            tail = tail.next
            listLen += 1            # count the nodes
        
        # Step 2: Figure out the index (from the start) of the node to delete
        deletingElemFromStart = listLen - n
        
        # Special case: if we need to delete the head node
        if deletingElemFromStart == 0:
            return head.next
        
        # Step 3: Traverse again to find the node to delete
        curr = head                 # current node we are checking
        prev = None                 # previous node (used to reconnect links)
        while deletingElemFromStart != -1:

            if deletingElemFromStart == 0:
                # We’ve reached the node to delete
                # Skip over it by linking prev to curr.next
                prev.next = curr.next
                return head          # return the modified list’s head
            else:
                # Keep moving forward until we reach the node to delete
                prev = curr
    
            # Step forward in the list
            deletingElemFromStart -= 1   
            curr = curr.next


    
    
# Helper function to create a linked list from a list
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert linked list to a Python list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    head = build_linked_list([1, 2, 3, 4, 5])
    n = 2
    new_head = solution.removeNthFromEnd(head, n)
    print("Output for [1,2,3,4,5] with n=2:", linked_list_to_list(new_head))
    
    # Example 2
    head = build_linked_list([1])
    n = 1
    new_head = solution.removeNthFromEnd(head, n)
    print("Output for [1] with n=1:", linked_list_to_list(new_head))
    
    # Example 3
    head = build_linked_list([1, 2])
    n = 1
    new_head = solution.removeNthFromEnd(head, n)
    print("Output for [1,2] with n=1:", linked_list_to_list(new_head))