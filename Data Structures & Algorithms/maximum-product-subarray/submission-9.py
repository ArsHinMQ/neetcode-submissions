class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        mini, maxi = 1, 1

        for n in nums:
            tmp = maxi * n
            maxi = max(tmp, n * mini, n)
            mini = min(n * mini, n, tmp)
            ans = max(ans, maxi)
        return ans
            
        


        