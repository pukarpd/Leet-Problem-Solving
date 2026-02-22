class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        mySet = {'b', 'a', 'l', 'o', 'n'}
        hashmap = {}

        for i in range(len(text)): 
            if text[i] in mySet and text[i] not in hashmap: 
                hashmap[text[i]] = 1
            elif text[i] in mySet and text[i] in hashmap: 
                hashmap[text[i]] += 1 
         
        if len(hashmap) < 5: 
            return 0 

        string = 'balloon'
        res = 0 
        ones, twos = {'b', 'a', 'n'} , {'l', 'o'}
        while True:  
            i = 0  
            while i < len(string): 
                if string[i] in hashmap and hashmap[string[i]] > 0: 
                    hashmap[string[i]] -= 1 
                    i += 1 
                else: 
                    break
            if i == 7 : 
                res += 1 
            else:  
                break

        return res





