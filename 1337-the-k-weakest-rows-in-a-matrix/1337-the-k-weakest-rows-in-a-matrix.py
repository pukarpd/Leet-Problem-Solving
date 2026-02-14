class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Solved using heaps(O(n) construct the array of tuples and O(k) to find the indices)
        weaker = [(sum(x), i) for i, x in enumerate(mat)]
        heapq.heapify(weaker)
        # print(weaker)

        res = []
        while k > 0: 
            heapVal = heapq.heappop(weaker)
            idx = heapVal[1]
            res.append(idx)
            k-=1 
        return res 

