class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # we only care about the triplets where at lease one value is below the target/ if theyre all above, we         dont        care, as max will not work. O(n) complexity

        skim = [] 
        x, y, z = target[0], target[1], target[2]
        for triplet in triplets: 
            ai, bi, ci = triplet[0], triplet[1], triplet[2]
            if ai > x or bi > y or ci > z: 
                continue
            else:
                skim.append(triplet)


        # print(skim)
        a = b = c = False 
        for triplet in skim:
            ai, bi, ci = triplet[0], triplet[1], triplet[2]
            if ai == x:
                a = True 
            if bi == y: 
                b = True 
            if ci == z: 
                c = True 

        return a and b and c




        # # brute force: O(n**2)
        # x, y, z = target[0], target[1], target[2]
        # for i in range(len(triplets)): 
        #     ai, bi, ci = triplets[i][0], triplets[i][1], triplets[i][2] 
        #     for j in range(i, len(triplets)): 
        #         aj, bj, cj  =  triplets[j][0], triplets[j][1], triplets[j][2] 
        #         triplets[j][0], triplets[j][1], triplets[j][2] = max(ai, aj), max(bi, bj), max(ci, cj)
        #         c1, c2, c3 = triplets[j][0], triplets[j][1], triplets[j][2]
        #         if c1 == x and c2 == y and c3 == z: 
        #             return True 

        
        # return False 