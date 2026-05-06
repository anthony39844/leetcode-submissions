class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        time = o(log(n))
        space = o(1)
        '''
        if len(nums) == 0:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        first, last = -1, -1
        while l <= r:
            x = (l + r) // 2
            if nums[x] == target:
                first = x
                r = x - 1
            elif nums[x] > target:
                r = x - 1
            else:
                l = x + 1
        
        if first == -1:
            return [first, last]
        
        l, r = 0, len(nums) - 1
        while l <= r:
            x = (l + r) // 2
            if nums[x] == target:
                last = x
                l = x + 1
            elif nums[x] > target:
                r = x - 1
            else:
                l = x + 1
        
        return [first, last]
