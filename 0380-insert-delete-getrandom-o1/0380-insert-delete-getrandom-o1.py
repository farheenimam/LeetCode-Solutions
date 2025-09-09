import random
class RandomizedSet(object):
    
    def __init__(self):
        self.RandomizedSet = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.RandomizedSet:
            return False    
        self.RandomizedSet.add(val)
        return True    
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.RandomizedSet:
            self.RandomizedSet.remove(val)
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        if (len(self.RandomizedSet)) != 0:
            return random.choice(list(self.RandomizedSet))
        return False    
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()