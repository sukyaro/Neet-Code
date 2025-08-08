
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # Storing all the strings in the list
        res = []

        # Checking that the string is valid, we keep track of the opening and closing brackets
        # And if the number of opening brackets is not equal to the number of closing brackets, the string is not valid
        def isValid(string):
            open = 0
            for symbol in string:
                if symbol == '(':
                    open += 1
                else:
                    open -= 1
                if open < 0:
                    return False
            if open == 0:
                return True
            else:
                return False
            
        # Creating a string
        def dfs(string):
            if len(string) == n * 2: # Checking that the length of the string is valid
                if isValid(string): # Checking that the string is valid
                    res.append(string) # Adding the string to the list if both validations are passed 
                return
            
            dfs(string + '(') # recursively calling the function to add another opening bracket
            dfs(string + ')') # recursively calling the function to add another closing bracket

        dfs("")
        return res

# A little test of the program
solution = Solution()
solution1 = solution.generateParenthesis(1)
solution2 = solution.generateParenthesis(3)
solution3 = solution.generateParenthesis(5)            

print(solution1)
print(solution2)
print(solution3)