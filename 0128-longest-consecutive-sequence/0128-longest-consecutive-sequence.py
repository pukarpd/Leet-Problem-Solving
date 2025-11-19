class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Neetcode solution, understood and learned about hashsets/sets again. DS part of DSA for this.
        numset = set(nums)
        longest = 0 

        for n in numset: 
            # check for start of sequence
            if (n-1) not in numset: 
                length = 0
                while (n + length) in numset:
                    length += 1 
                longest = max(length, longest) 
        return longest



        # Attempted solution that only works for positive integers at a limit, binning approach i thought of in the moment implemented. Not memory optimal but O(n) time complexity. 
        # if nums == None:
        #     return 0 
        # if nums == []: 
        #     return 0 

        # maxValue = max(nums)
       
        # bins = ["No"] * (maxValue + 1) 
      
        # for num in nums:  
        #     bins[num] = num
        # # print(bins)
        # maxVal = 0 
        # maxConsec = 0
        # i = 0
        # while i < len(bins): 
        #     if bins[i] != "No": 
        #         maxConsec += 1 
        #     else: 
        #         maxConsec = 0
        #     i += 1 
        #     maxVal = max(maxVal, maxConsec)

        # return maxVal

        # for key, value in hasher.items(): 
