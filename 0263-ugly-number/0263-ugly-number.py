import math
class Solution:
    def isUgly(self, n: int) -> bool:
        # neetcode solution
        if n <= 0: 
            return False 
        if n == 1 or n == 2 or n == 3 or n == 5: 
            return True

        for p in [2,3,5]: 
            while n % p == 0:
                n = n // p
        return n == 1 
    






















        # # Approach still didnt work, tried making some tweaks. If a number ends with 0, its automatically out
        # # if it ends with an even number, it should also automatically be out right? or not who knows
        # # looking up the solution. 
        # if n == 0: 
        #     return False
        
        # if n == 1: 
        #     return True 

        # if n == 2 or n == 3 or n == 5: 
        #     return True
        

        # if n < 0: 
        #     return False
        


        # # approach didnt work/ TLE or MLE or both. There has to be a better way. 
        # dictionary = {}

        # # no other way to solve this with basic syntax unless you know the sieve of eratosthenes
        # # ancient algorithm for finding all prime numbers for any given limit. 
        # def sieve_of_eratosthenes (lime): 
        #     primes = [True] * (lime + 1) 
        #     primes[0], primes[1] = False, False
        #     for num in range(2,int(lime ** 0.5) + 1): 
        #         if primes[num]: 
        #             for multiple in range (num * num, lime + 1, num): 
        #                 primes[multiple] = False 
            
        #     return [num for num, is_prime in enumerate(primes) if is_prime]

        # dictionary = {}
        # comparison_arr = sieve_of_eratosthenes(int(math.sqrt(n)))
       
        # comparison_arr = sieve_of_eratosthenes(int(n/1000))
        
        # print(comparison_arr)

        # for item in comparison_arr:
        #     dictionary[item] = 0 

        # for item in dictionary: 
        #     if n % item == 0: 
        #         dictionary[item] += 1 
        
        # # print(dictionary)
        # count_ugly = 0 
        # count_beauty = 0
        # keys = [2,3,5]
        # for key, val in dictionary.items(): 
        #     if key in keys and val == 1:
        #         count_ugly += 1
        #     elif key not in keys and val == 1:
        #         count_beauty += 1 
        # print(count_ugly, count_beauty)
        
        # if count_ugly == 0 and count_beauty == 0: 
        #     return True
        # if count_ugly > 0 and count_beauty == 0: 
        #     return True 


        # return False   


        