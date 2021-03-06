#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = None
        go = True
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j] and \
                    (k is None or nums[j] < nums[k]):
                    k = j
            if k is not None:
                (nums[i], nums[k]) = (nums[k], nums[i])
                nums[i+1:] = sorted(nums[i+1:])
                break
        if k is None:
            nums.sort()
            go = False
        return go
        #return nums

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [tuple(nums)]
        while self.nextPermutation(nums):
            t = tuple(nums)
            if t == res[-1]:
                continue
            res.append(t)
        return map(list, res)

if __name__ == '__main__':
    s = Solution()
    print s.permuteUnique([1,1,2])
    print s.permuteUnique([3,3,0,0,2,3,2])
