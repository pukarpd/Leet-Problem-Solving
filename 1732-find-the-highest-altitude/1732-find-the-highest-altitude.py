class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0] * (len(gain) + 1)
        suma = 0 
        for i in range(len(gain)): 
            suma += gain[i]
            prefix[i+1] = suma
        
        # print(prefix)

        return(max(prefix))
