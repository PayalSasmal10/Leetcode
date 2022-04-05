from collections import OrderedDict
from linecache import cache

class LRUCache:

    def __init__(self, limit:int) -> None:
        self.cache = OrderedDict()
        self.limit = limit
    
    # checking the key is present or not and also checked if it is present then add 
    # that value to end for recently used
    def get(self, key):
        if key not in self.cache:
            return -1

        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.limit:
            self.cache.popitem(last = False)


cache_check = LRUCache(2)
cache_check.put(1,1)
print(cache_check.cache)
cache_check.put(2,2)
print(cache_check.cache)
cache_check.get(1)
print(cache_check.cache)
cache_check.put(3,3)
print(cache_check.cache)


