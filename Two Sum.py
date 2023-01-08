class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexesList = []
        j = 1
        for i in range(len(nums)):
            if nums[i] + nums[j] == target:
                indexesList.append(i)
                indexesList.append(j)
                break
            j = j + 1
        print(indexesList)
