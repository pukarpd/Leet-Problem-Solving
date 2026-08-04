class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_range, max_range = min(nums), max(nums)
        mySet = set([i for i in range(min_range, max_range+1)])
        comp = set([num for num in nums])
        new_set = mySet - comp
        return sorted(list(new_set))
