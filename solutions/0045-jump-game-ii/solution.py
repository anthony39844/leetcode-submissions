class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        start
        we set a window for start + 1 --> farthest index reachable
        then we loop through this window and set another window
        repeat

        '''

        l = r = 0
        out = 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            print(farthest, l , r)
            l = r + 1
            r = farthest
            out += 1

        return out
