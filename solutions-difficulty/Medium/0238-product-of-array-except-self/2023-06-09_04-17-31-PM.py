import array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        total = 1
        has_zero = False
        zeroes = 0
        for num in nums:
            if num != 0:
                total *= num
            elif num == 0: #checking if their are zeroes
                has_zero = True
                zeroes += 1
        for i in nums:
            if has_zero:
                if i != 0:
                    answer.append(0)
                else:
                    if zeroes == 1: #if there is only one zero 
                        answer.append(total)
                    elif zeroes > 1:
                        answer.append(0)
            else:
                if i != 0:
                    answer.append(int(total * (i ** -1)))
                else:
                    answer.append(int(total))
        return answer

