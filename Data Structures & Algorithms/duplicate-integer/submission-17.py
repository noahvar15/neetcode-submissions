class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        print(s)
        return (len(nums) != len(s))