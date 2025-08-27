
class TimeMap:

    def __init__(self):
        # Setting 2 dictionaries for storing values and all the timestamps for the same value
        self.time = {}
        self.previousStamp = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Setting the value and the timestamp for the key
        self.time.setdefault(key, {})
        self.time[key][timestamp] = value
        
        # Setting the timestamp for the key
        self.previousStamp.setdefault(key, []).append(timestamp)
        return None

    def get(self, key: str, timestamp: int) -> str:

        # If the key has not been set returning a null-string
        if key not in self.time:
            return ""
        
        # If the key with the right timestamp has been set, returning it
        if timestamp in self.time[key]:
            return self.time[key][timestamp]
        
        # If the key exists but the right timestamp has not been set looking for the nearest timestamp which is <= than the right one
        for t in range(len(self.previousStamp[key]) - 1, -1, -1):
            if self.previousStamp[key][t] <= timestamp:
                return self.time[key][self.previousStamp[key][t]]
            
        # Returning a null-string if none of the above apply
        return ""



# A little test of the program
solution = ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
# solution = ["TimeMap", "set", ["key1", "value1", 10], "get", ["key1", 1], "get", ["key1", 10], "get", ["key1", 11]]
# solution = ["TimeMap", "set", ["test", "one", 10], "set", ["test", "two", 20], "set", ["test", "three", 30], "get", ["test", 15], "get", ["test", 25], "get", ["test", 35]]

for i in range(len(solution) - 1):
    if solution[i] == "TimeMap":
        timeMap = TimeMap()
    
    if solution[i] == 'set':
        print(timeMap.set(*solution[i + 1]))
    
    if solution[i] == 'get':
        print(timeMap.get(*solution[i + 1]))
        