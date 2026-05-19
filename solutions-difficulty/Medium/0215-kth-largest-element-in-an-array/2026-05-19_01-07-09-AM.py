class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # init the heap with k elements
        heap = nums[:k]
        heapq.heapify(heap)

        # replace the min element with new num if larger than min
        # this will get rid of the smallest elements and only leave a min heap of the k largest elements
        for i in nums[k:]:
            if i > heap[0]:
                heapq.heappushpop(heap, i)
            
        return heap[0]

