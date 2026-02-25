class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashmap = {l : [] for l in s}

        for i, l in enumerate(s): 
            hashmap[l].append(i)

        for k, v in hashmap.items(): 
            vMax, vMin = max(v), min(v) 
            hashmap[k] = [vMin, vMax]
         
        # arr = [v for v in hashmap.values()]
        # arr.sort()
        # # print(arr,'\n',hashmap)

        maxEnd = [s[0], hashmap[s[0]][1]]

        res = []
        j = 0
        for i, l in enumerate(s):
            curEnd = hashmap[l][1]
            
            if curEnd >= maxEnd[1] and l != maxEnd[0]: 
                maxEnd[0] = l 
                maxEnd[1] = curEnd 

            if i == maxEnd[1]: 
                myString = s[j:i+1]
                # print(myString)
                res.append((i-j+1))
                j = i+1
            

        # print(res)

        return res 
            








        

