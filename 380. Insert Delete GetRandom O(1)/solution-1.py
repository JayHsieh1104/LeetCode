class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mDict = {}
        self.mList = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mDict:
            return False
        else:
            self.mList.append(val)
            self.mDict[val] = len(self.mList) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.mDict:
            self.mList[self.mDict[val]], self.mDict[self.mList[-1]] = self.mList[-1], self.mDict[val]
            del self.mList[-1]
            del self.mDict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.mList) 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()