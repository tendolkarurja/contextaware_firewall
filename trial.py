class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n + 1)

        def helper(step):
            if step <= 3:
                return step
            if dp[step] != -1:
                return dp[step]
            dp[step] = helper(step -1) + helper(step -2)
            return dp[step]
        
        return helper(n)
        #n = 4
        #dp[4] = 3 + 2
        #