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

        cur = self.head
        while cur.key != key:
            cur = cur.next

        if key == self.head.key:
            if self.count > 1:
                self.head = self.head.next
            else:
                return self.cache[key]
        elif key == self.tail.key:
            return self.cache[key]
        else:
            # connecting the prev and next of cur node to each other
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

        # adding MRU to the end of list
        self.tail.next = cur
        cur.next = None
        cur.prev = self.tail
        self.tail = self.tail.next

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return
        if self.count == 0:
            self.head = ListNode(key)
            self.tail = self.head
        else:
            self.tail.next = ListNode(key, prev=self.tail)
            self.tail = self.tail.next
            if self.count >= self.cap: # we need to evict LRU item
                del self.cache[self.head.key]
                self.head = self.head.next
                self.count -= 1
        
        self.cache[key] = value
        self.count += 1

class ListNode():
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next
