from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        self.dict = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.dict[val].add(len(self.list))
        self.list.append(val)
        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.dict[val]:
            return False
        else:
            remove_pos, last_num = self.dict[val].pop(), self.list[-1]
            self.list[remove_pos] = last_num
            self.dict[last_num].add(remove_pos)
            self.dict[last_num].discard(len(self.list) - 1)
            
            self.list.pop()
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.list[random.randint(0, len(self.list)-1)]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()