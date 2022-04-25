# First Negative Integer in every window size of k

size = 8
arr = [12, -1, -7, 8, -15, 30, 16, 28]
# o/p = [-1, -1, -7, -15, -15, 0] o/p should be len(arr) - k + 1

# 1st approach: O(n^2) time complexity
class subArrays:
    new_list = []
    def sub_array(self,arr, k=3):
        for i in range(len(arr)-k):
            for j in range(i, i+k):
                if arr[j] < 0:
                    self.new_list.append(arr[j])
                    break
                
            
        return self.new_list


sub = subArrays()
print(sub.sub_array(arr))

print("..............................................")      

#2nd approach: O(n) time complexity 
class subArrays1:
    new_list = []
    output = []
    def sub_array1(self,arr, k=3):
        i = j = 0

        while(j<len(arr)):
            if arr[j] < 0:
                    self.new_list.append(arr[j]) 

            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                if len(self.new_list) == 0:
                     self.output.append(0)
                else:
                    self.output.append(self.new_list[0])
                    if arr[i] == self.new_list[0]: 
                        self.new_list.pop(0)


                
                i += 1
                j += 1

        return self.output



sub1 = subArrays1()
print(sub1.sub_array1(arr))







