
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        tempRange = []

        # Going through every element of the list
        for i in range(len(temperatures)):
            day = temperatures[i]
            counter = 0 # setting the counter
            for j in range(i, len(temperatures)):
                newDay = temperatures[j]
                if newDay > day:
                    counter = j - i
                    break
            tempRange.append(counter)



        ## Alternative way, using a stack
        #res = [0] * len(temperatures)
        #stack = []

        #for i, t in enumerate(temperatures):
        #    while stack and t > stack[-1][0]:
        #        stackT, stackInd = stack.pop()
        #        res[stackInd] = i - stackInd
        #    stack.append((t, i))

        #return res


        return tempRange 
                

# A little test of the program
solution = Solution()
solution1 = solution.dailyTemperatures([30,38,30,36,35,40,28])
solution2 = solution.dailyTemperatures([22,21,20])

print(solution1)
print(solution2)
