# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, stair: list[int]) -> int:
        n, memo = len(stair), {}
        stair.append(0)
        def memoize(n):
            if n == 0 or n == 1: return stair[n]
            elif n in memo: return memo[n]
            memo[n] = stair[n] + min(memoize(n - 1), memoize(n - 2))
            return memo[n]
        return memoize(n)
        
sol = Solution()
print(sol.minCostClimbingStairs(stair = [10,15,20]))
print(sol.minCostClimbingStairs(stair = [1,100,1,1,1,100,1,1,100,1]))