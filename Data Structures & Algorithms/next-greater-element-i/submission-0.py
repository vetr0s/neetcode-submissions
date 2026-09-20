class Solution:
    def greaterElement(self, nums: List[int], start: int) -> int:
        res = -1
        cur_num = nums[start]
        for i in range(start, len(nums)):
            if nums[i] > cur_num:
                return nums[i]
        return -1
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for num in nums1:
            res = self.greaterElement(nums2, nums2.index(num))
            out.append(res)
        return out