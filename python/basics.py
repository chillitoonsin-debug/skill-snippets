"""Python bite-sized snippets."""

# 1. Flatten a nested list
def flatten(nested):
    out = []
    for item in nested:
        if isinstance(item, list):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out

# 2. Chunk a list
def chunk(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

# 3. Retry decorator
import time, functools

def retry(times=3, delay=0.5):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **k):
            last = None
            for _ in range(times):
                try:
                    return fn(*a, **k)
                except Exception as e:
                    last = e
                    time.sleep(delay)
            raise last
        return wrapper
    return deco

# 4. Memoize
def memoize(fn):
    cache = {}
    @functools.wraps(fn)
    def wrapper(*a):
        if a not in cache:
            cache[a] = fn(*a)
        return cache[a]
    return wrapper
