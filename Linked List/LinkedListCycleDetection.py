
from typing import Optional

# The test is written by Chat-GPT to be able to test the program myself the way neet code does it
# Definition for singly-linked list (LeetCode style).
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using the fast/slow aproach where the slow pointer moves one forward at a time and the fast pointer moves 2 elements
        slow, fast = head, head
        
        # Going thorough the list
        while fast and fast.next:
            slow = slow.next # Moving slow by 1
            fast = fast.next.next # Moving fast by 2
            if slow == fast:
                return True
        
        return False



def create_linked_list_with_cycle(values, pos):
    """
    values: list of node values
    pos: index where tail connects (-1 for no cycle)
    """
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    nodes = [head]
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
        nodes.append(curr)
    if pos != -1:
        curr.next = nodes[pos]  # create cycle
    return head

def test():
    sol = Solution()

    # Case 1: [3,2,0,-4], pos=1 (cycle at node with value 2)
    head1 = create_linked_list_with_cycle([3,2,0,-4], 1)
    print("Test 1 (cycle):", sol.hasCycle(head1))  # Expected True

    # Case 2: [1,2], pos=0 (cycle at head)
    head2 = create_linked_list_with_cycle([1,2], 0)
    print("Test 2 (cycle):", sol.hasCycle(head2))  # Expected True

    # Case 3: [1], pos=-1 (no cycle)
    head3 = create_linked_list_with_cycle([1], -1)
    print("Test 3 (no cycle):", sol.hasCycle(head3))  # Expected False

    # Case 4: [], empty list
    head4 = create_linked_list_with_cycle([], -1)
    print("Test 4 (empty):", sol.hasCycle(head4))  # Expected False
    
    # Case 5: [1, 2, 3, 4], pos = 1 (cycle)
    head5 = create_linked_list_with_cycle([1, 2, 3, 4], 1)
    print("Test 5 (cycle):", sol.hasCycle(head5))  # Expected True

if __name__ == "__main__":
    test()
