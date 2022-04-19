class Solution:
        
    def cal_permute(self,index,nums,output):
        if index == len(nums):
            output.append(nums)
            #print(output)
            return
        
        for i in range(index,len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            #print("nums :", nums)
            self.cal_permute(index+1, nums, output)
            nums[index], nums[i] = nums[i], nums[index]
            #print("index : ", index, "i :", i)
            #print("after recursion : ", nums)
    print(output)


nums = [1,2,3]
output = []
s = Solution()
s.cal_permute(0,nums,output)

