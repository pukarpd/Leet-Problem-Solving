class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 1: 
            return True 

      


        newstring = ""

        for i in range(len(s)): 
            if s[i].isalnum():
                newstring += s[i].lower()
        
        if len(newstring) == 0: 
            return True
                

        i = 0
        j = len(newstring) - 1  
      
        while  i < (len(newstring) - 1) / 2 : 
            if newstring[i] != newstring[j]:
                return False
            i += 1 
            j -= 1 
        
        print(i)
        print(j)

        mybooleanCheck = newstring[i] == newstring[j]
       
    
        return mybooleanCheck


        