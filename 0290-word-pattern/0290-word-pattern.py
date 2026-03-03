class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern2 = s.split(' ')
        # print(pattern2)
        return self.pattern(pattern) == self.pattern(pattern2)
        
    def pattern(self, p): 
        pl = defaultdict(list)

        for i in range(len(p)): 
            pl[p[i]].append(i)
 

        return sorted([val for val in pl.values()])