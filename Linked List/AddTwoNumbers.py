from typing import Optional

# The test is written by Chat-GPT to be able to test the program myself the way neet code does it
# Definition for singly-linked list (LeetCode provides this automatically).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1, number2 = "", "" # Storing the numbers
        
        # Going through every diget of number 1 and adding it to the string
        curr1 = l1
        while curr1:
            number1 += str(curr1.val)
            curr1 = curr1.next
            
        # Going through every diget of number 2 and adding it to the string
        curr2 = l2
        while curr2:
            number2 += str(curr2.val)
            curr2 = curr2.next
            
        # Getting the right number and creating a new linked list to store it 
        newNumber = str(int(number1[::-1]) + int(number2[::-1]))
        nextNode = None
        for i in range(len(newNumber)):
            curr = ListNode(int(newNumber[i]))
            curr.next = nextNode
            nextNode = curr
        
        # Returning the new list
        return nextNode
            
            
            
    

def print_linked_list(node):
    """Helper to print linked list in readable format"""
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))

def build_linked_list(numbers):
    """Helper to build linked list from a list of integers"""
    dummy = ListNode(0)
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Example test cases
if __name__ == "__main__":
    # Example 1: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])

    # Call the function under test
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print("Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)")
    print("Expected Output: 7 -> 0 -> 8")
    print("Your Output:   ", end="")
    print_linked_list(result)

    # Example 2: (0) + (0)
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])

    result = solution.addTwoNumbers(l1, l2)
    print("\nInput: (0) + (0)")
    print("Expected Output: 0")
    print("Your Output:   ", end="")
    print_linked_list(result)

    # Example 3: (9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9) + (9 -> 9 -> 9 -> 9)
    l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_linked_list([9, 9, 9, 9])

    result = solution.addTwoNumbers(l1, l2)
    print("\nInput: (9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9) + (9 -> 9 -> 9 -> 9)")
    print("Expected Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1")
    print("Your Output:   ", end="")
    print_linked_list(result)
    
    # Example 4: (1 -> 2 -> 3) + (4 -> 5 -> 6)
    l1 = build_linked_list([1, 2, 3])
    l2 = build_linked_list([4, 5, 6])

    result = solution.addTwoNumbers(l1, l2)
    print("\nInput: (1 -> 2 -> 3) + (4 -> 5 -> 6)")
    print("Expected Output: 5 -> 7 -> 9")
    print("Your Output:   ", end="")
    print_linked_list(result)