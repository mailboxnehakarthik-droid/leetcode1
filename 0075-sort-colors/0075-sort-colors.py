class Solution(object):
    def sortColors(self, nums):
        lst0 = []
        lst1 = []
        lst2 = []
        
        for i in nums:
            if i == 0:
                lst0.append(i)
            elif i == 1:
                lst1.append(i)
            elif i == 2:
                lst2.append(i)
        
        lst0.extend(lst1)
        lst0.extend(lst2)

        for i in range(len(nums)):
            nums[i] = lst0[i]