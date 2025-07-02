

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        valid = True

        # Checking that there are no duplicats in each row of the matrix
        for i in board:
            dic1 = {}
            for j in i:

                # Only adding the digits to the dictionary
                if j != '.':
                    dic1[j] = dic1.setdefault(j, 0) + 1

                    # Checking if the element is already in the dictionary
                    if dic1.get(j) > 1:
                        valid = False
                        break
                        
        
        # Checking for any duplicates in each column
        for i in range(len(board)):
            dic2 = {}
            for j in range(len(board)):
                currentElem = board[j][i]

                # Only adding the digits to the dictionary
                if currentElem != ".":
                    dic2[currentElem] = dic2.setdefault(currentElem, 0) + 1

                    # Checking if the element is already in the dictionary
                    if dic2.get(currentElem) > 1:
                        valid = False
                        break
                

        # Checking for duplicates in each 3x3 sub-box
        for i in range(3): # Iterate over 3 block rows
            for m in range(3): # Iterate over 3 block columns
                dic3 = {}
                for j in range(3): # Row indedx inside the 3x3 box
                    for k in range(3): # Column index inside the 3x3 box
                        currentElem = board[i * 3 + j][m * 3 + k]
                        if currentElem != ".":
                            dic3[currentElem] = dic3.setdefault(currentElem, 0) + 1
                            if dic3.get(currentElem) > 1:
                                valid = False
                                break


        return valid

 
# A small test of the program
solution = Solution()

solution1 = solution.isValidSudoku([["1","2",".",".","3",".",".",".","."],
                                    ["4",".",".","5",".",".",".",".","."],
                                    [".","9","8",".",".",".",".",".","3"],
                                    ["5",".",".",".","6",".",".",".","4"],
                                    [".",".",".","8",".","3",".",".","5"],
                                    ["7",".",".",".","2",".",".",".","6"],
                                    [".",".",".",".",".",".","2",".","."],
                                    [".",".",".","4","1","9",".",".","8"],
                                    [".",".",".",".","8",".",".","7","9"]])


solution2 = solution.isValidSudoku([["1","2",".",".","3",".",".",".","."],
                                    ["4",".",".","5",".",".",".",".","."],
                                    [".","9","1",".",".",".",".",".","3"],
                                    ["5",".",".",".","6",".",".",".","4"],
                                    [".",".",".","8",".","3",".",".","5"],
                                    ["7",".",".",".","2",".",".",".","6"],
                                    [".",".",".",".",".",".","2",".","."],
                                    [".",".",".","4","1","9",".",".","8"],
                                    [".",".",".",".","8",".",".","7","9"]])


print(solution1)
print(solution2)
