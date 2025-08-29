class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        right product and left product
        [1, 2, 3, 4]
        -->
        [1, 1, 2, 6]
        this is the left product

        for the right product we do
        [1, 2, 3, 4]
        -->
        [24, 12, 4, 1]

        now multiply them together

        [1, 1, 2, 6]
        [24, 12, 4, 1]
        [24, 12, 8, 6]

        so for the left product, each index holds the value of all the numbers left of that index multiplied to each other
        the first index defaults to 1
        and same goes for the right product except that its all the numbers to the right of that index
        so when we multiply those 2 arrays together we get the numbers of both sides not including the self index
        '''

        right = 1
        arr = []
        for i in nums:
            arr.append(right)
            right *= i
        
        left = 1
        arr2 = []
        for i in range(len(nums) - 1, -1, -1):
            arr2.append(left)
            left *= nums[i]

        for i in range(len(nums)):
            arr[i] *= arr2[len(arr2) - i - 1]
        
        return arr
        
        
