class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub = 0
        hashmap = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in hashmap:
                return [hashmap[sub],i]
            else :
                hashmap[nums[i]] = i