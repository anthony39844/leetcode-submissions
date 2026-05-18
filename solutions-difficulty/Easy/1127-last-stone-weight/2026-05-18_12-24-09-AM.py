class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        nums = [-i for i in stones]

        heapq.heapify(nums)

        while len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            if x == y:
                continue
            else:
                heapq.heappush(nums, -y - -x)
        
        return -nums[0] if len(nums) > 0 else 0

