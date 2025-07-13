
class MinStack:

    def __init__(self):
        # Setting the empty stack and using an array for storing the minimum value
        self.stack = []
        self.minimum = []


    def push(self, val: int) -> None:
        # When we push a value onto the stack we also add it to the minimum array and sort that array
        self.stack.append(val)
        self.minimum.append(val)
        self.minimum.sort()


    def pop(self) -> None:
        # First of all when were poping a value, we delete it from the minimum array
        # Deleting the first element in the minimum array if it is the one at the top of the stack
        if self.stack[-1] == self.minimum[0]:
            del self.minimum[0]
        
        # If the element at the top of the stack is not the first element in the minimum array
        # We implement sequential search to find the element in the array and delete it
        elif self.stack[-1] in self.minimum:
            for i in range(len(self.minimum)):
                if self.minimum[i] == self.stack[-1]:
                    del self.minimum[i]
                    break
        
        # Deleting the top element of the stack
        del self.stack[-1]


    def top(self) -> int:
        # Returning the top element of the stack
        return self.stack[-1]
    

    def getMin(self) -> int:
        # Returning the minimum element in the stack
        return self.minimum[0]


# A little test of the program
input = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
input = ["MinStack", "push", 1, "push", 2, "push", -2, "push", -1, "push", -2, "push", 3, "pop", "top", "getMin", "pop", "getMin", "pop", "top", "getMin", "pop", "top", "getMin", "pop", "getMin"]

def run_the_data_structure(input):
    output = []

    for i in range(len(input)):
        if input[i] == "MinStack":
            solution = MinStack()
            output.append(None)
        elif input[i] == "push":
            output.append(None)
            solution.push(input[i + 1])
        elif input[i] == "pop":
            output.append(None)
            solution.pop()
        elif input[i] == "top":
            output.append(solution.top())
        elif input[i] == "getMin":
            output.append(solution.getMin())

    return output

print(run_the_data_structure(input))