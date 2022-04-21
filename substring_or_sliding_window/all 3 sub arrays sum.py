class subArrays:
    def sub_array(self,strings, k=3):
        i = j = 0
        sum = 0
        max_val = strings[0]
        new_list = []
        new_list1 = []
        for i in range(len(strings)-3):
            for j in range(i, i+3):
                new_list.append(strings[j])
                sum += strings[j]
                max_val = max(max_val,sum)
                # new_list1.append(new_list)
            print(new_list)
            sum = 0
            new_list = []
        
        return max_val
        

strings = [2, 3, 5, 2, 9, 7, 1]

s = subArrays()
print(s.sub_array(strings))