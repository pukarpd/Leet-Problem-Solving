class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = dict()
        for num in arr: 
            if num in hashmap: 
                hashmap[num] += 1 
            else: 
                hashmap[num] = 1 
        arr1 = [val for val in hashmap.values()]
        mySet = set(arr1)

        return len(mySet) == len(arr1)
