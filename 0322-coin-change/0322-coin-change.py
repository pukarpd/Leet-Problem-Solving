'''You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) 

and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount.

If it is impossible to make up the amount, return -1.

Constraints: len(coins) == 10
coins[i] is dynamic, it scales all the way to 2^30 - 1 == 1,073,741,824 - 1. IT is not a fixed sized coins, but rather the value of the coins grow. 

We can also use an unlimited number of each coin. This problem has a recurrence relation of combination sum. 
Maybe we can check for each coin, loop through and add, then pop after we reach a certain amount, or we can skip a combination entirely if it exceeds
the min length we have in our res. 
If we sort coins, we can iterate from the back to the front, so base case would be if i == 0: return, and if sum(subarray) after appending and recurring, return

Use amount to keep track

Example: 
coins[1,5,10] , amt = 12. 

sort coins, take 10, take 10 again. Oops, give 10 back, go to 5. take 5 oops, give 5, go to 1. 

coins[11, 22, 33, 44, 55, 66, 77, 88, 99, 111] amt = 330, expected = 4. 3 88s and a 66. my algorithm probably starts from 111, takes 2, then 
the resulting diff is 108 which means its impossible from there on out given what we have. keep taking, if negative, move to the next i. pop originals
pop next i, once we reach 0 break. append to res as we go. Brute force O(2**n) 

Guarenteed TLE. 
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # O(amount * len(coins)), memory O(amount). new pattern
        dp = [float("inf")] * (amount+ 1) 
        dp[0] = 0

        for a in range(1, amount+1): 
            for c in coins: 
                if a - c >= 0: 
                    dp[a] = min(dp[a], 1 + dp[a - c]) #recrrence relation 

        return dp[amount] if dp[amount] != float("inf") else -1


        # #works but inefficient, pruned brute force still not good enough. O(n** t)
        # coins.sort(reverse = True)
        # print(coins)
        # res = []
        # minResLen = float("inf")
        # def all_coin_combinations(start: int, amount: int, subarr: List): 
        #     # print(f"{start}\t{amount}\t{subarr}")
        #     nonlocal minResLen
        #     if amount == 0: 
        #         res.append(subarr[:])
        #         minResLen = min(minResLen, len(subarr))
        #         return
        #     if amount < 0: 
        #         return 
        #     for i in range(start, len(coins)): 
        #         subarr.append(coins[i])
        #         if len(subarr) < minResLen:
        #             all_coin_combinations(i, amount - coins[i], subarr)
        #         else: 
        #             subarr.pop()
        #             continue
        #         subarr.pop()

        # all_coin_combinations(0, amount, [])

        # # print(res)
        # return min(len(x) for x in res) if res else -1

        # # Greedy doesnt work
        # coins.sort()
        # total = 0
        # amt = amount 
        # for i in range(len(coins)-1,-1,-1): 
        #     diff = amt
        #     while diff > 0: 
        #         diff = diff - coins[i]
        #         total += 1 
        #     if diff < 0: 
        #         diff += coins[i]
        #         total -= 1 
        #     amt = diff 
        # return total if amt == 0 else -1

