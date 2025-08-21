class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0 
        # floyds algorithm
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break
            
        # Phase two of the algorithm
        slow2 = 0
        while True: 
            # advance the slow pointer by one, as well as the second slow pointer
            # slow will advance by x
            slow = nums[slow]
            # slow 2 will meet slow 1 at the convergence point, p, which is the beginning of the cycle as well as the result   
            slow2 = nums[slow2]

            if slow  == slow2: 
                return slow2 
        
        # neetcode solution, runs in linear time, constant space (just slow and slow2 being advanced)


    



        
                
