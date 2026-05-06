class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        right = left + (k - 1)
        max_window = []

        for i in range(right + 1):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        max_window = [nums[queue[0]]]

        while right < len(nums) - 1:
            left += 1
            right += 1

            # Remove elements outside the current window from the front of the deque
            if queue[0] < left:
                queue.popleft()

            # Add the next element to the deque
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            queue.append(right)

            max_window.append(nums[queue[0]])

        return max_window
        

"""
        left = 0
        right = left + (k - 1)
        queue = sorted(nums[left: right + 1])
        max_window = []

        if k == 1:
            return nums

        while True:
            max_window.append(queue[-1])
            right += 1
            left += 1
            if right == len(nums):
                break
            if nums[right] > queue[k - 1] and queue[-1] in nums[left: right + 1]:
                queue.pop(0)
                queue.append(nums[right])
            else:
                queue = sorted(nums[left: right + 1])

        return max_window
"""        
"""
        max_window = []
        left = 0
        right = left + (k - 1)
        window = nums[left: right + 1]
        max_num = max(window)

        if k == 1:
            return nums

        while right < len(nums):
            if nums[right] < max_num and max_num in nums[left: right + 1]:
                max_window.append(max_num)
                left += 1
                right += 1
                continue
            else:
                window = nums[left: right + 1]
                max_num = max(window)
                max_window.append(max_num)
                left += 1
                right += 1
            
        return max_window
        """
        

