class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0

        while True: 
            if num1 <= 0 or num2 <= 0: 
                break
            if num1 >= num2: 
                num1 = num1 - num2 
                operations += 1 
            elif num2 >= num1:
                num2 = num2 - num1
                operations += 1



    
        return operations