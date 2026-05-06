class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = list(range(2))
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                arr[0] = left + 1
                arr[1] = right + 1
                return arr
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
