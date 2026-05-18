class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        # shrink min heap to only the last k elements (the top k largest elements)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # heap is not of size
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        # incoming val is greater than the smallest of the top k, pop and push new val onto heap
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
