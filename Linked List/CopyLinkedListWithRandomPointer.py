
from typing import Optional

# The test is written by Chat-GPT to be able to test the program myself the way neet code does it
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None: # Checking if the list is empty and returning None if it is
            return None
        
        newNodes = {} # Creating a HashMap to store the nodes
        
        # Going through the nodes and creating new coppies of the nodes
        curr = head
        while curr:
            newNodes[curr] = Node(curr.val)
            curr = curr.next

        # Going through the nodes again and adding the pointers to the new nodes
        curr = head
        while curr:
            newNode = newNodes[curr]
            newNode.next = newNodes.get(curr.next)
            newNode.random = newNodes.get(curr.random)
            curr = curr.next
            
        # Returning the new nodes
        return newNodes[head]
            
        
        
    

def print_list(head: 'Node'):
    """Helper function to print the list with next and random pointers."""
    nodes = []
    while head:
        rand_val = head.random.val if head.random else None
        nodes.append(f"({head.val}, random={rand_val})")
        head = head.next
    print(" -> ".join(nodes))

# ---------- TEST CASE ----------
if __name__ == "__main__":
    # Create original list
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    # Setup next pointers
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Setup random pointers
    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    print("Original list:")
    print_list(node1)

    # Call your solution here
    solution = Solution()  # <-- your class
    copied_head = solution.copyRandomList(node1)

    print("\nCopied list:")
    print_list(copied_head)