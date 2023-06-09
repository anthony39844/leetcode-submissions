import array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        total = 1
        has_zero = False
        zeroes = 0
        for num in nums:
            if num != 0: 
                total *= num #if the num is not a 0 multiply it by the total
            elif num == 0: #checking if their are zeroes
                has_zero = True
                zeroes += 1
        for i in nums:
            if has_zero: #if there are zeroes
                if i != 0: #if the num is not a zero
                    answer.append(0) #append a 0 because if there are 0s then the product is 0
                else: #if the num is a zero
                    if zeroes == 1: #if there is only one zero 
                        answer.append(total) #append the total because the product is all the numbers besides that 0 so the product is not 0 but the total
                    elif zeroes > 1: #if there is more than one 0
                        answer.append(0) #append a 0 because the product will be 0 again
            else: #if there are no zeroes
                answer.append(int(total * (i ** -1)))
        return answer

