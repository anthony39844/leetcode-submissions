class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        sorted_dict = dict()
        for i in range(len(nums)):
            one = nums[i]
            if one > 0:
                break
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] + one < 0:
                    left += 1
                elif nums[left] + nums[right] + one > 0:
                    right -= 1
                else:
                    key = tuple([one, nums[left], nums[right]])
                    if key not in sorted_dict:
                        sorted_dict[key] = 1
                        out.append(key)
                    right -= 1

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
                

