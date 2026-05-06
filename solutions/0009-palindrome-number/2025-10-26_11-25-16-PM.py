class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        nums = deque()
        i = x
        while i > 0:
            nums.append(i % 10)
            i = i // 10

        while nums:
            if len(nums) == 1:
                return True
            if nums.popleft() != nums.pop():
                return False
        
        return True
