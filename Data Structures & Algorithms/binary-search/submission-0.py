class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        mid = lo + (hi - lo) // 2
        res = -1

        def bsearch(lo, hi):
            if lo > hi:
                return -1
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bsearch(mid+1, hi)
            elif nums[mid] > target:
                return bsearch(lo, mid-1)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            res = bsearch(mid+1, hi)
        elif nums[mid] > target:
            res = bsearch(lo, mid-1)

        return res
        
        