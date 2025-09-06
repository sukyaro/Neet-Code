

class LRUCache:

    def __init__(self, capacity: int):
        # Setting the dictionary for the processes, the maximum capacity, and tracker of the recent processes
        self.cache = {}
        self.allowedCapacity = capacity
        self.lastRecent = [] # This is used as a queue

    def get(self, key: int) -> int:
        if key in self.cache: # Checking if the process has been put before
            if key in self.lastRecent: # Checking if the key is already in the tracker
                self.lastRecent.remove(key) # Removing the key if its in the tracker
            self.lastRecent.append(key) # Adding the key to the end of the queue
            return self.cache[key]
        else:
            return - 1
        

    def put(self, key: int, value: int) -> None:
        # Checking if the process has already been addded to the queue and removing it if it has
        if key in self.lastRecent:
            self.lastRecent.remove(key)
            self.allowedCapacity += 1
            
        # If the capacity is full removing the least recent process
        if self.allowedCapacity == 0:
                self.cache.pop(self.lastRecent[0])
                del self.lastRecent[0]
                self.allowedCapacity += 1
        
        # Adding the process to the queue, setting its value in the dictionary and decrementing the free copacity
        self.lastRecent.append(key)    
        self.cache[key] = value
        self.allowedCapacity -= 1
        


# A little test of the program
# solution = ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
# solution = ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]
# solution = ["LRUCache", [2], "get", [2], "put", [2, 6], "get", [1], "put", [1, 5], "put", [1, 2], "get", [1], "get", [2]]
# solution = ["LRUCache", [3], "put", [1, 1], "put", [2, 2], "put", [3, 3], "get", [1], "get", [2], "get", [4], "put", [4, 4], "get", [1], "get", [2], "get", [3], "get", [4], "get", [2], "put", [1, 8], "put", [3, 7], "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get", [2], "get", [3], "get", [4], "put", [1,9], "put", [6,6], "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get", [6]]
solution = ["LRUCache", [10], "put", [10, 13], "put", [3, 17], "put", [6, 11], "put", [10, 5], "put", [9, 10], "get", [13], "put", [2, 19], "get", [2], "get", [3], "put", [5, 25], "get", [8], "put", [9, 22], "put", [5, 5], "put", [1, 30], "get", [11], "put", [9, 12], "get", [7], "get", [5], "get", [8], "get", [9], "put", [4, 30], "put", [9, 3], "get", [9], "get", [10], "get", [10], "put", [6, 14], "put", [3, 1], "get", [3], "put", [10, 11], "get", [8], "put", [2, 14], "get", [1], "get", [5], "get", [4], "put", [11, 4], "put", [12, 24], "put", [5, 18], "get", [13], "put", [7, 23], "put", [8, 27], "put", [12, 12], "get", [3], "put", [3, 21], "put", [10, 10], "get", [8], "get", [11], "get", [7], "put", [7, 10], "put", [9, 2], "put", [5, 8], "get", [11], "put", [8, 2], "put", [11, 1], "put", [5, 5], "get", [5], "put", [4, 9], "get", [4], "get", [10], "put", [6, 18], "put", [4, 7], "put", [8, 12], "get", [7], "get", [5], "get", [4], "get", [5], "put", [7, 23], "get", [3], "put", [7, 3], "put", [4, 4], "put", [10, 6], "get", [6], "put", [3, 9], "get", [3], "get", [4], "put", [11, 11], "put", [1, 12], "get", [3], "put", [1, 2], "put", [5, 6], "get", [5], "put", [1, 11], "put", [8, 12], "get", [2], "get", [5], "get", [9], "put", [10, 1], "put", [1, 3], "get", [10], "put", [10, 2], "put", [1, 11], "put", [5, 5], "put", [7, 5], "put", [10, 10], "get", [9], "get", [4], "get", [4], "get", [6], "get", [11], "put", [7, 13], "put", [2, 7], "put", [10, 13], "put", [8, 5], "put", [9, 10], "get", [6], "get", [10], "put", [3, 5], "put", [10, 12], "put", [5, 12], "get", [8], "get", [3], "put", [3, 1], "put", [4, 6], "put", [10, 4], "put", [8, 10], "put", [4, 9], "put", [2, 13], "put", [10, 8], "put", [1, 8], "put", [1, 2], "put", [4, 6], "put", [4, 2], "put", [10, 10], "put", [9, 12], "get", [4], "get", [10], "get", [10], "get", [9], "put", [8, 7], "get", [5], "put", [3, 8], "get", [10], "put", [5, 11], "put", [5, 2], "get", [8], "put", [1, 3], "put", [7, 8], "get", [1], "put", [6, 5], "get", [9], "put", [7, 12], "get", [5], "get", [8], "put", [10, 4], "put", [1, 9], "put", [2, 4], "put", [2, 5], "put", [10, 10], "get", [5], "get", [9], "get", [10], "put", [8, 3], "put", [1, 7], "put", [10, 7], "put", [4, 8], "put", [2, 11], "put", [8, 2], "get", [1], "get", [9], "get", [2], "put", [2, 5], "put", [3, 8], "put", [1, 8], "put", [2, 7], "get", [10], "get", [3], "put", [1, 4], "put", [10, 5], "get", [8], "get", [2], "get", [2], "get", [1], "put", [9, 2], "get", [5], "get", [7], "put", [10, 3], "put", [5, 5], "put", [1, 10], "put", [2, 10], "get", [4], "get", [3], "get", [1], "get", [1], "put", [3, 7], "get", [9], "put", [10, 2], "get", [3], "get", [4], "put", [6, 4], "get", [6], "put", [7, 11], "get", [8], "get", [6], "put", [2, 2], "get", [2], "put", [7, 9], "put", [8, 6], "put", [2, 4], "get", [8], "get", [1], "put", [7, 5], "put", [4, 1], "get", [10], "put", [6, 3], "get", [6], "put", [4, 6], "put", [1, 8], "put", [6, 7], "put", [3, 4], "put", [4, 3], "get", [10], "get", [3], "get", [7], "put", [4, 3], "get", [8], "put", [3, 7], "get", [4], "get", [10], "put", [6, 4], "put", [5, 10], "put", [2, 4], "put", [5, 6], "put", [10, 9], "put", [5, 8], "put", [1, 3], "put", [7, 5], "put", [8, 10], "get", [3], "put", [6, 4], "get", [5], "put", [8, 2], "put", [8, 7], "put", [6, 4], "get", [10], "put", [9, 3], "put", [4, 7], "get", [6], "put", [5, 10], "get", [10], "get", [10], "put", [8, 5], "get", [4], "put", [5, 9], "put", [9, 9], "put", [5, 2], "put", [6, 4], "put", [3, 8], "put", [8, 8], "put", [10, 2], "put", [2, 7], "put", [1, 7], "put", [10, 9], "get", [4], "get", [1], "get", [7], "put", [8, 10], "get", [6], "put", [4, 5], "get", [7], "put", [3, 9], "get", [4], "get", [1], "put", [6, 9], "put", [10, 10], "put", [9, 1], "put", [4, 6], "put", [1, 10], "get", [8], "put", [7, 10], "get", [9], "put", [5, 5], "put", [1, 3], "get", [8], "put", [2, 7], "get", [9], "put", [6, 4], "get", [7], "put", [2, 9], "get", [10], "get", [6]]


for i in range(len(solution) - 1):
    if solution[i] == "LRUCache":
        capacity = solution[i + 1][0]
        lru = LRUCache(capacity)
    
    if solution[i] == 'put':
        print(lru.put(*solution[i + 1]))
        # lru.put(*solution[i + 1])
    
    if solution[i] == 'get':
        print(lru.get(*solution[i + 1]))
        # lru.get(*solution[i + 1])