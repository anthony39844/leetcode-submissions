class Solution:
    def findMin(self, nums: List[int]) -> int:
            # 0 1 2 3 4 5 6 
            # 1 2 3 4 5 6 0 
            # 2 3 4 5 6 0 1
            # 3 4 5 6 0 1 2
            #.      l m.  r
            #.      l mr
            # 4 5 6 0 1 2 3
            # 5 6 0 1 2 3 4
            # 6 0 1 2 3 4 5
        left, right = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[right]: #means it is not rotated
            return nums[0]
        else:
            while left < right:
                mid = (left + right) // 2
                if left + 1 == right:
                    if nums[left] > nums[right]:
                        return nums[right]
                    else:
                        return nums[left]
                elif nums[mid] < nums[right]:
                    right = mid
                elif nums[mid] > nums[right]:
                    left = mid





            
        

            

