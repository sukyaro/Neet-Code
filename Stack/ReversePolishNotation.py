
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # Initialising an empty stack to store the operands and the results
        stack = []

        # Going through all elements in the list
        for i in range(len(tokens)):
            currElement = tokens[i]

            # Checking that the current token is an operator
            if currElement == '+' or currElement == '-' or currElement == '*' or currElement == '/':

                # Popping the 2 values from the stack for the operation
                value1 = stack.pop() # The second operand
                value2 = stack.pop() # The first operand

                if currElement == "+":
                    stack.append(value2 + value1) # Add and push the result
                elif currElement == '-':
                    stack.append(value2 - value1) # Subtract and push the result
                elif currElement == '*':
                    stack.append(value2 * value1) # Multilpy and push the result
                else:
                    stack.append(int(value2 / value1)) # Divide and push the result (were using int() to truncate towards zero)
                
            else:
                # If its a number, converting it to int and pushing onto the stack
                stack.append(int(currElement))

        # Returning the final result which is stored as the first element in the stack    
        return stack[0]


# A little test of the program
solution = Solution()
solution1 = solution.evalRPN(["1","2","+","3","*","4","-"])
solution2 = solution.evalRPN(["4","13","5","/","+"])
solution3 = solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

print(solution1)
print(solution2)
print(solution3)

