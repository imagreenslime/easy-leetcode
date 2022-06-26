# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        def memoize(n, memo):
            if n in memo:
                return memo[n]
            elif n == 0 or n == 1:
                result = 1
            else:
                result = memoize(n - 1, memo) + memoize(n - 2, memo)
            memo[n] = result
            return result
        memo = {}
        return memoize(n, memo)

sol = Solution()
print(sol.climbStairs(5))
