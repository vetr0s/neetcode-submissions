class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val -> idx
        for idx,val in enumerate(nums):
            need = target - val
            if need in seen:
                return [seen[need], idx]
            seen[val] = idx
            