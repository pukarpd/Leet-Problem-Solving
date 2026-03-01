class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        ans = [str(i) for i in range(1,n+1)]

        for k, s in enumerate(ans):
            i = int(s)
            if i % 3 == 0 and i % 5 != 0: 
                ans[k] = "Fizz"
            if i % 5 == 0 and i % 3 != 0: 
                ans[k] = "Buzz"
            if i % 3 == 0 and i % 5 == 0: 
                ans[k] = "FizzBuzz"

        return ans 
