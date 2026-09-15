class MyHashSet:

    def __init__(self):
        self.empty_set = set()

    def add(self, key: int) -> None:
        self.key = key
        self.empty_set.add(key)
        

    def remove(self, key: int) -> None:
        self.key = key
        self.empty_set.discard(key)
        

    def contains(self, key: int) -> bool:
        self.key = key
        if key in self.empty_set:
            return True
        else :
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)