class Solution:
    def climbStairs(self, n: int) -> int:
        dp = defaultdict(int)
        def memo( n ):
            if n in dp: 
                return dp[n]
            if n == 1:
                dp[n] = 1 
                return 1
            if n == 2: 
                dp[n] = 2
                return 2 

            val = memo(n-2) + memo(n-1)
            dp[n] = val
            return val

        return memo(n)