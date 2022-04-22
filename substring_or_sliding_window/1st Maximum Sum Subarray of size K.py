# o(n^2) time complexity
class subArrays:
    def sub_array(self,strings, k=3):
        i = j = 0
        sum = 0
        max_val = strings[0]
        new_list = []
        for i in range(len(strings)-k):
            for j in range(i, i+k):
                new_list.append(strings[j])
                sum += strings[j]
                max_val = max(max_val,sum)
                # new_list1.append(new_list)
            print(new_list)
            sum = 0
            new_list = []
        
        return max_val
        

strings = [2, 3, 5, 2, 9, 7, 10]

s = subArrays()
print(s.sub_array(strings))
print("...............................")
# o(n) time complexity
class subArrays1:
    def sub_array1(self,strings, k=3):
        i = j = 0
        sum = 0
        max_val = strings[0]
        new_list = []
        while(i<=len(strings)-k):
            if j < i+k:
                sum += strings[j]
                max_val = max(sum, max_val)
                new_list.append(strings[j])
                j += 1
            elif j <= i+k:
                i += 1
                j = i
                print(new_list)
                sum = 0
                new_list = []

        return max_val


sa = subArrays1()
print(sa.sub_array1(strings))

print("........................................")
# 3rd approach
class subArrays2:
    def sub_array2(self,strings, k=3):
        i = j = 0
        sum = 0
        max_val = strings[0]
        while(j<len(strings)):
            sum += strings[j]

            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                max_val = max(sum, max_val)
                sum = sum - strings[i]
                i += 1
                j += 1
        return max_val


sub2 = subArrays2()
print(sub2.sub_array2(strings))


