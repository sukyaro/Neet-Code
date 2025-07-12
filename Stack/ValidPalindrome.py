
class Solution:
    def isValid(self, s: str) -> bool:
        
        # It's a completed dictionary for all possible inputs where the kes are the closing brackets and the values are
        # the opening brackets
        readyDict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        # Making a variable for the length of the string and the empty stack
        stringLength = len(s)
        listOfSymbols = []

        # If the string has an odd number of characters it is impossible that it has a valid parentheses
        if stringLength % 2 != 0:
            return False
        
        # If the string is empty then it does not have a valid parentheses
        if stringLength == 0:
            return False


        for i in s:
            # If the first element of the string is a closing bracket then the string does not have a valid parentheses
            if len(listOfSymbols) == 0 and (i == ')' or i == '}' or i == ']'):
                return False
            
            # If the char is a closing bracket checking that at the top of the stack there is the right type of the opening bracket
            elif i == ')' or i == '}' or i == ']':
                if listOfSymbols[-1] != readyDict[i]:
                    return False
                else:
                    del listOfSymbols[-1]

            # If the char is an opening bracket then we push it onto the stack
            else:
                listOfSymbols.append(i)
            
        # If the stack is empty at the end and the returning function has not been called that means
        # that the string has a valid parentheses
        if len(listOfSymbols) == 0:
            return True
        else:
            return False

        
# A little test of the program
solution = Solution()

solution1 = solution.isValid("([{}])")
solution2 = solution.isValid("[]")
solution3 = solution.isValid("[(])")
 

print(solution1)
print(solution2)
print(solution3)