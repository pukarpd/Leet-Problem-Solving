class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}


        for s in strs: 
            new_str = ''.join(sorted(s))
            hashmap[new_str] = []

        for s in strs: 
            new_str = ''.join(sorted(s))
            hashmap[new_str].append(s)

        res = [] 

        for v in hashmap.values(): 
            res.append(v)

        return res



        
        # res = [] 

        # seen = set()
        
        # for i in range(len(strs)): 
        #     temp = [] 
        #     if i in seen: 
        #         continue
        #     temp.append(strs[i])
        #     for j in range(i + 1, len(strs)): 
        #         if sorted(strs[i]) == sorted(strs[j]): 
        #             seen.add(j)
        #             temp.append(strs[j])
        #     res.append(temp)

        # return res
            

            

            
