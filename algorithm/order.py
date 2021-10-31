# -*- coding: utf-8 -*-

from typing import List

class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        sort 与 sorted 区别：
        sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
        list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
        """
        return sorted(num*num for num in nums)


    def sortedSquaresMerge(self, nums: List[int]) -> List[int]:
        """
        有序数组归并排序
        """
        negative = -1
        n = len(nums)
        for i,num in enumerate(nums):
            if num < 0:
                negative = i;
            else:
                break

        ans = list()
        i,j = negative,negative+1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(nums[j] * nums[j])
                j += 1
            elif j==n:
                ans.append(nums[i] * nums[i])
                i -= 1
            elif (nums[i] * nums[i]) < (nums[j] * nums[j]):
                ans.append(nums[i] * nums[i])
                i -= 1
            else:
                ans.append(nums[j] * nums[j])
                j += 1
        return ans

    def bubbleSort(self,nums: List[int]) ->  List[int]:
        """
        冒泡排序
        """
        n = len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if(nums[j] > nums[j+1]):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        return nums

    def selectionSort(self,nums: List[int]) -> List[int]:
        """
        选择排序
        """
        n = len(nums)
        for i in range(n-1):
            minIndex = i
            for j in range(i+1,n-1):
                if(nums[j] < nums[minIndex]):
                    minIndex = j
            temp = nums[i]
            nums[i] = nums[minIndex]
            nums[minIndex] = temp
        return nums
    
    def insertionSort(self,nums: List[int]) -> List[int]:
        """
        插入排序
        """
        n = len(nums)
        for i in(1,n-1):
            preIndex,current = i-1,nums[i]
            while( (preIndex >=0) and (nums[preIndex] > current)):
                nums[preIndex + 1] = nums[preIndex]
                preIndex -= 1            
            nums[preIndex + 1] = current
        return nums
    
    def shellSort(self,nums:List[int]) -> List[int]:
        """
        希尔排序
        """
        return

    def quickSort(self,nums: List[int]) -> List[int]:
        """
        快速排序
        """
        return

    def mergeSort(self,nums: List[int]) -> List[int]:
        """
        无序数组归并排序
        """
        return
    




# nums = [-1,0,3,5,9,12]
nums0 = [-5,-3,-2,-1,0,12]
nums = [9,-3,5,-1,0,-12]

x = Solution()
print("print result:",x.sortedSquares(nums0))
print("print result:",x.sortedSquaresMerge(nums0))
print("print result:",x.bubbleSort(nums))
print("print result:",x.selectionSort(nums))
print("print result:",x.insertionSort(nums))
print("print result:",x.shellSort(nums))
print("print result:",x.quickSort(nums))