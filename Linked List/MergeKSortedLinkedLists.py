
from typing import Optional

# The test is written by Chat-GPT to be able to test the program myself the way neet code does it
# Definition for singly-linked list (LeetCode provides this automatically).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    # Helper to convert linked list to Python list (for easy comparison)
    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result



class Solution:    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = None # Assigning a none variable to be in the first comparison
        
        # going through all the linked lists
        for i in range(len(lists)):
            dummy = self.mergeTwoLists(dummy, lists[i]) # Compare the 2 lists and save the result in a variable dummy
            
        return dummy
    
    # This approach does not create a new list, it just changes the pointers of the existing nodes
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Implementing a dummy sorting algorithm
        dummy = curr = ListNode()
        
        # Going through the 2 lists and adding the smaller values
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
            
        # Dealing with leftovers
        curr.next = l1 or l2
    
        return dummy.next
                
                
            
    

# --- Test harness ---
def build_linked_list(values):
    """Helper: builds a linked list from a Python list."""
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(node):
    """Helper: prints linked list as a Python list."""
    if not node:
        print([])
    else:
        print(node.to_list())


if __name__ == "__main__":
    # Example test cases
    # lists = [
    #     build_linked_list([1, 4, 5]),
    #     build_linked_list([1, 3, 4]),
    #     build_linked_list([2, 6])
    # ]
    
    # lists = [
    #     build_linked_list([1, 2, 4]),
    #     build_linked_list([1, 3, 5]),
    #     build_linked_list([3, 6])
    # ]
    
    # lists = []
    # lists = [[]]

    solution = Solution()
    merged = solution.mergeKLists(lists)

    print("Merged result:")
    print_linked_list(merged)  # Expected: [1,1,2,3,4,4,5,6]