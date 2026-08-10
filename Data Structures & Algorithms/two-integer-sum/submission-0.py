class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n=len(nums)

        ts={}

        for i in range(n):
            need=target-nums[i]

            if need in ts:
                return [ts[need],i]

            ts[nums[i]]=i
        return[]
        