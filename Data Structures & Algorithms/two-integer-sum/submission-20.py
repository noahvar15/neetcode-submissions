class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        res = []

        # {(3, 0)}
        # i = 1, num = 4
        # 7 - 4 = 3
        # dif = 3
        # differneces(3) = 0
        
        for i, num in enumerate(nums):
            dif = target - num
            if dif in differences:
                res = [min(differences[dif], i), max(differences[dif], i)]
            differences[num] = i
        return res