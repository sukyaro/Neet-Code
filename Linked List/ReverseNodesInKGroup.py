
from typing import Optional

# The test is written by Chat-GPT to be able to test the program myself the way neet code does it
# Definition for singly-linked list (LeetCode provides this automatically).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Calculating the length of the list
        lenPointer = head
        listLen = 0
        while lenPointer:
            listLen += 1
            lenPointer = lenPointer.next
            
        # Creating a dummy node to handle edge cases
        dummy = ListNode(0, head)
        curr = head
        groupPrev = dummy
            
        # Processing each full group of size k
        for i in range(listLen // k):
            prev = None
            newHead = curr
            
            for i in range(k):
                next = curr.next # Storing the next node
                curr.next = prev # Reverding the link
                prev = curr # Move the previous one step forward
                curr = next # Move the curr one steo forward

            # Conecting the reversed group back to the list
            groupPrev.next = prev # Linking the previous group to the new head
            newHead.next = curr # Linking the new tail to the next segment
            
            # Moving groupPrev to the end of the reversed group
            groupPrev = newHead
            

        return dummy.next
                


# Helper function: Convert list to linked list
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


# Helper function: Convert linked list back to Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# --------- Test Cases ---------
if __name__ == "__main__":
    sol = Solution()

    # Test 1
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 2
    result = sol.reverseKGroup(head, k)
    print("Test 1:", linked_list_to_list(result))  # Expected: [2, 1, 4, 3, 5]

    # Test 2
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 3
    result = sol.reverseKGroup(head, k)
    print("Test 2:", linked_list_to_list(result))  # Expected: [3, 2, 1, 4, 5]

    # Test 3
    head = build_linked_list([1, 2])
    k = 2
    result = sol.reverseKGroup(head, k)
    print("Test 3:", linked_list_to_list(result))  # Expected: [2, 1]

    # Test 4
    head = build_linked_list([1])
    k = 1
    result = sol.reverseKGroup(head, k)
    print("Test 4:", linked_list_to_list(result))  # Expected: [1]

    # Test 5
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    k = 4
    result = sol.reverseKGroup(head, k)
    print("Test 5:", linked_list_to_list(result))  # Expected: [4, 3, 2, 1, 5, 6]
