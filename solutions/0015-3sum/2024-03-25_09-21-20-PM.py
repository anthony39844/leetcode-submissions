class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) 
        out = []
        sorted_dict = dict()
        for i in range(len(nums)):
            one = nums[i] #first number
            if one > 0: #this is because if the list is sorted then there is no way for the number to add up to 0 if the first number is greater than 0
                break
            if i > 0 and nums[i] == nums[i - 1]: #if we are at the same number as before then skip to the next number
                continue
                
            left = i + 1 
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] + one < 0: #if sum is less than 0, increase the left pointer
                    left += 1
                elif nums[left] + nums[right] + one > 0: #is greater than 0, decrease the right pointer
                    right -= 1
                else:
                    key = tuple([one, nums[left], nums[right]]) #else we make a key with as tuple of our values
                    if key not in sorted_dict: #if it is not already in the dict
                        sorted_dict[key] = 1 #then we add it to the dicitonary
                        out.append(key) #and we append it to our output
                    left += 1 #we increase the left pointer so we can keep looping
                    while nums[left] == nums[left - 1] and left < right: #if we are the same number then we just continute
                        left += 1

        return out



        # if len(nums) < 2:
        #     return [[]]
        # one, two, three = 0, 1, 2
        # out = []
        # while one + 2 < len(nums):
        #     if nums[one] + nums[two] + nums[three] == 0:
        #         ans = [nums[one], nums[two], nums[three]]
        #         if tuple(sorted(ans)) not in out:
        #             out.append(tuple(sorted(ans)))
        #     while two + 1< len(nums):
        #         if nums[one] + nums[two] + nums[three] == 0:
        #             ans = [nums[one], nums[two], nums[three]]
        #             if tuple(sorted(ans)) not in out:
        #                 out.append(tuple(sorted(ans)))
        #         while three < len(nums):
        #             if nums[one] + nums[two] + nums[three] == 0:
        #                 ans = [nums[one], nums[two], nums[three]]
        #                 if tuple(sorted(ans)) not in out:
        #                     out.append(tuple(sorted(ans)))
        #             three += 1
        #         two+=1
        #         if two + 1 < len(nums):
        #             three = two + 1
        #     one += 1
        #     if one + 1 < len(nums):
        #         two = one + 1
        #     if two + 1 < len(nums):
        #         three = two + 1
                
        #return out
                

