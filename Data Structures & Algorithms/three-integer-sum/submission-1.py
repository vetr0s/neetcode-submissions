class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx,val in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            l,r = idx+1, len(nums) - 1
            target = -val
            while l < r:
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res