class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0,0]
        distances = [self.l2norm(point, origin) for point in points]

        hashmap = {val:[] for val in distances}

        for i, val in enumerate(distances):
            hashmap[val].append(i) 
        # print(distances,"\n",hashmap)
        heapq.heapify(distances)
        res = []
        for _ in range(k): 
            min_d= heapq.heappop(distances)

            res.append(hashmap[min_d])
        idx = set()
        for item in res: 
            for x in item: 
                idx.add(x)
        # print(idx)

        return [points[x] for x in idx]

    def l2norm(self, arr1, arr2): 

        return math.sqrt(((arr1[0] - arr2[0]) ** 2) + ((arr1[1] - arr2[1]) ** 2))