class MyHashSet:

    def __init__(self):
        self._data = set()
        

    def add(self, key: int) -> None:
        self._data.add(key)

    def remove(self, key: int) -> None:
        self._data.discard(key)
        

    def contains(self, key: int) -> bool:
        if key in self._data:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)