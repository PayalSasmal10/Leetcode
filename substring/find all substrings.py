# o(n^2) time complexity

strings = "payal"
strings = "payal"
sub_str = []
class subStrings:
    def substring(self,strings):
        for i in range(len(strings)):
            add = strings[i]
            sub_str.append(strings[i])
            for j in range(i+1,len(strings)):
                add += strings[j]
                sub_str.append(add)
        print(sub_str)
    
s = subStrings()
s.substring(strings)
    
#p pa pay paya payal 
strings = "payal"
print("here",strings[:-1:])

# o(n) time complexity and space complexity
class substrings:
    def substrings_func(self,strings):
        k = 0
        l = k
        new_list = []
        test = ""
        while(k<len(strings)):
            print(k)
            if l<len(strings):
                test += strings[l]
                new_list.append(test)
                l += 1
            if l >= len(strings):
                k += 1
                l = k
                test = ""
        print(new_list)

s1 = substrings()
s1.substrings_func(strings)





    