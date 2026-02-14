class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        hashmap = {val: i for i, val in enumerate(score)}

        score_heap = [-x for x in score]
        heapq.heapify(score_heap)
        awards = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        res = score
        print(res)
        for i, s in enumerate(score): 
            largest = -heapq.heappop(score_heap)
            if i < 3: 
                res[hashmap[largest]] = awards[i]
            else: 
                res[hashmap[largest]] = str(i+1)
            
        return res
