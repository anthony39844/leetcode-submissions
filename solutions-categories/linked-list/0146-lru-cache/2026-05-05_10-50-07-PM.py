class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.count = 0
        self.cache = {}
        self.tail = None
        self.head = None
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        cur = self.cache[key]
        if key== self.tail.key:
            return self.cache[key].val
      # If it's the head, shift the head pointer forward
        if cur == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            # It's in the middle: disconnect it from its neighbors
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

        # Append 'cur' to the tail
        self.tail.next = cur
        cur.prev = self.tail
        cur.next = None
        self.tail = cur

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return
        x = ListNode(key, value)
        if self.count == 0:
            self.head = x
            self.tail = self.head
        else:
            x.prev = self.tail
            self.tail.next = x
            self.tail = self.tail.next
            if self.count >= self.cap: # we need to evict LRU item
                del self.cache[self.head.key]
                self.head = self.head.next
                self.count -= 1
        
        self.cache[key] = x
        self.count += 1

class ListNode():
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
