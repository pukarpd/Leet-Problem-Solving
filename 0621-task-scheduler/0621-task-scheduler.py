class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        # Could not figure out. 
        hashmap = {}
        for task in tasks:
            if task not in hashmap:  
                hashmap[task] = 1
            else: 
                hashmap[task] += 1 

        print(hashmap)
        a = max(val for val in hashmap.values())
        c = 0
        for k, v in hashmap.items(): 

            if v == a: 
                print(k)
                c += 1 
        print(a,c)

        return max(len(tasks), (a-1) * (n+1) + c)



            
