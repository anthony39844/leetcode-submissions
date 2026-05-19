class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for i in nums[k:]:
            if i > heap[0]:
                heapq.heappushpop(heap, i)
            
        return heap[0]

