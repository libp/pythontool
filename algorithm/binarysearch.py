#!/usr/bin/env python
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



nums,target = [-1,0,3,5,9,12],9
x = Solution()
print("print result:",x.search(nums,target))
