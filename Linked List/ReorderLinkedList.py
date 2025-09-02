
from typing import Optional

# The test is written by Chat-GPT to be able to test the program myself the way neet code does it
# Definition for singly-linked list (LeetCode provides this automatically).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finding the middle of the list useing the slow/fast pointers
        l1, l2 = head, head # starting at the head, in the end l1 will be pointing at the middle of the list and l2 will be pointing at the end of the list
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next

        # Reversing the second part of the list
        prev, curr, nextN = None, l1.next, None
        l1.next = None # separating the first half of the linked list from the second one
        while curr:
            nextN = curr.next # saving the next node
            curr.next = prev # reversing the link
            prev = curr # moving previous to the current
            curr = nextN # moving current to the next one
        
        # merging the 2 linked lists
        newCurr = head
        while prev:
            nextNode1 = newCurr.next # saving the next element in the first part
            nextNode2 = prev.next # saving the next element in the second part
            newCurr.next = prev # connecting the first part with the second one
            prev.next = nextNode1 # connecting the second part with the first one
            newCurr = nextNode1 # moving along the first part
            prev = nextNode2 # moving along the second part 
            
            


def build_linked_list(values):
    """Build a linked list from a list of values and return the head."""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def linked_list_to_list(head):
    """Convert a linked list back to a Python list for easy checking."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def print_linked_list(head):
    """Pretty print the linked list."""
    values = linked_list_to_list(head)
    print(" -> ".join(map(str, values)))

# ----------------------
# Test Harness
# ----------------------

def test_reorder_list():
    sol = Solution()  # <-- Your solution class with reorderList method

    # # Case 1: [1,2,3,4] -> expected reorder [1,4,2,3]
    # head1 = build_linked_list([1,2,3,4])
    # sol.reorderList(head1)
    # print("Test 1:", linked_list_to_list(head1))  # Expected [1,4,2,3]

    # Case 2: [1,2,3,4,5] -> expected reorder [1,5,2,4,3]
    head2 = build_linked_list([1,2,3,4,5])
    sol.reorderList(head2)
    print("Test 2:", linked_list_to_list(head2))  # Expected [1,5,2,4,3]

    # # Case 3: [1,2] -> expected reorder [1,2]
    # head3 = build_linked_list([1,2])
    # sol.reorderList(head3)
    # print("Test 3:", linked_list_to_list(head3))  # Expected [1,2]

    # # Case 4: [1] -> expected reorder [1]
    # head4 = build_linked_list([1])
    # sol.reorderList(head4)
    # print("Test 4:", linked_list_to_list(head4))  # Expected [1]

if __name__ == "__main__":
    test_reorder_list()