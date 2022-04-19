class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        output = []
        def cal_prem(index, nums):
            if index == len(nums):
                if nums not in output:
                    output.append(list(nums))
            
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                cal_prem(index+1, nums)
                nums[index], nums[i] = nums[i], nums[index]
                
        cal_prem(0,nums)
        return output


        