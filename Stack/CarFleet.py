
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Merging positions and speeds of the cars
        newPositions = [[position[i], speed[i]] for i in range(len(position))]

        # Sorting the positions/speeds in descending order
        newPositions.sort(reverse=True)
        
        # Calculating the time for each car to get to the target
        times = list(map(lambda x: (target - x[0]) / x[1], newPositions))

        # Setting the number of fleeds and the last fleed time
        fleets = 0
        lastFleet = -1

        # Going through the times and if the current car's time is bigger than the last fleet adding a new fleet
        for i in times:
            if i > lastFleet:
                fleets += 1
                lastFleet = i

        return fleets
    

        # The same but using stacks
        # fleetStack = [[times[0]]]
        # stackPointer = 0

        # for i in range(len(times)):
        #     if times[i] <= fleetStack[stackPointer][-1]:
        #         fleetStack[stackPointer].append(times[i])
        #     else:
        #         fleetStack.append([times[i]])
        #         stackPointer += 1

        # return len(fleetStack)


# A little test of the program
solution = Solution()
solution1 = solution.carFleet(10, [1, 4], [3, 2])
solution2 = solution.carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1])
solution3 = solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
solution4 = solution.carFleet(10, [3], [3])
solution5 = solution.carFleet(100, [0, 2, 4], [4, 2, 1])
solution6 = solution.carFleet(16, [11, 14, 13, 6], [2, 2, 6, 7])

print(solution1)
print(solution2)
print(solution3)
print(solution4)
print(solution5)
print(solution6)

# Some thoughts
# the algorithm works for the target time
# now i need to adjust it so that it also works when the cars catch up not reaching the target
