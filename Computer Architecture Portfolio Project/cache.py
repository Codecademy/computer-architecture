import collections

CACHE_SIZE = 16


# This class implements the cache of the CPU as defined in the portfolio project outline document
class Cache:
    # The actual cache is implemented as a python d.e. queue, by 'appending' we mimic the LFU behavior required.
    # Inside of the d.e. queue, we are storing tuples of the format (<address>,<value>)
    def __init__(self):
        self.cache = collections.deque(maxlen=CACHE_SIZE)
        self.flush_cache()

    # Repeatedly append to the cache to flush the cache
    def flush_cache(self):
        for i in range(CACHE_SIZE):
            self.cache.append(("", ""))

    def search_cache(self, address):
        for i in range(CACHE_SIZE):
            if self.cache[i][0] == address:
                return self.cache[i][1]
        return None

    def write_cache(self, address, value):
        self.cache.append(tuple((address, value)))
