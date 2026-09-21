class Solution:
    def binary_search(self, lo: int, hi: int, nums: List[int], target: int) -> int:
        if lo > hi:
            return -1
        mid = lo + (hi - lo) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binary_search(mid+1, hi, nums, target)
        return self.binary_search(lo, mid-1, nums, target) 
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums)-1, nums, target)

        