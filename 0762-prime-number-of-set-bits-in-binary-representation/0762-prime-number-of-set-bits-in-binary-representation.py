class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        largest_bits = bin(right)[2:]
        compare = len(largest_bits) * "1"

        # Time complexity: 0(n * sqrt(k)) but sqrt(k) is tiny as number of set bits wont exceed 32
        # or worst case 64. here it wont exceed 32 because 10^6.    
        # print(type(largest_bits))
        res = 0 
        for i in range(left, right+1): 
            curBit = bin(i)[2:]
            extra_padding = len(largest_bits) - len(curBit)
            width = len(curBit) + extra_padding

            padded_bit = format(i, f"0{width}b")
            # print(curBit, extra_padding, padded_bit)

            ones = (int(padded_bit, 2) & int(compare, 2)).bit_count()
            # print(i, padded_bit, ones)
            res += 1 if self.isPrime(ones) else 0
        
        return res


    
    def isPrime (self, n: int) -> bool: 
        if n < 2: 
            return False 
        if n % 2 == 0: 
            return n == 2   

        i = 3 
        while i * i <= n: 
            if n % i == 0: 
                return False
            i += 2 
        return True 

             