# -*- coding: utf-8 -*-

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ans = list()
        for i in range(n):
            ans.append(nums[(i+k)%n])
        return ans

    

k,nums = 3,[-5,-3,-2,-1,0,12]

x = Solution()
print("print result:",x.rotate(nums,k))