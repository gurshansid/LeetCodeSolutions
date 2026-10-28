class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        if val not in self.hmap:
            self.hmap[val] = len(self.numList)
            self.numList.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.hmap:
            index = self.hmap[val]
            last = self.numList[-1]
            self.numList[index] = last
            self.hmap[last] = index
            self.numList.pop()
            del self.hmap[val]
            return True
        else:
            return False
        
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()