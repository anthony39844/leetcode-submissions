class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return [max(nums)]

        out = []
        q = deque()
        l, r = 0, 0

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            if q[0] == l - 1:
                q.popleft()
            if r + 1 >= k:
                l += 1
                out.append(nums[q[0]])
            r += 1

        return out


        

