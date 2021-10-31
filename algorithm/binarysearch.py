# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,height = 0,len(nums)-1
        while low <= height:
            mid = (height - low) // 2 + low
            num = nums[mid]
            if num == target:
                return mid
            elif num > target :
                height = mid - 1
            else:
                low = mid + 1
        return -1

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right=1,n
        while left < right:
            mid = (right-left)//2 + left
            # if isBadVersion(mid):
            if mid > 4 :
                right = mid
            else:
                left= mid + 1
        return left
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left <= right:
            mid = (right+left)//2 
            if (nums[mid]>target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
            else:
                return mid
        return left;


nums,target = [-1,0,3,5,9,12],9
x = Solution()
print("print result:",x.search(nums,target))
