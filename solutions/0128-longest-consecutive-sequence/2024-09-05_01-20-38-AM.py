class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        n = sorted(nums)
        m = 0
        curr_m = 1
        for i in range(0, len(n) - 1):
            if n[i + 1] == n[i]:
                continue
            elif n[i] + 1 == n[i + 1]:
                curr_m += 1
                continue
            else:
                m = max(curr_m, m)
                curr_m = 1
        return max(curr_m, m)
