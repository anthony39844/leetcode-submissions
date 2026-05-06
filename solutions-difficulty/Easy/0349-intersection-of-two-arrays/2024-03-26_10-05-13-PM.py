class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        l = min(len(nums1), len(nums2))
        for i in range(l):
            if nums1[i] in nums2:
                set1.add(nums1[i])
            if nums2[i] in nums1:
                set1.add(nums2[i])
        return set1
        
