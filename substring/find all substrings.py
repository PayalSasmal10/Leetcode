# o(n^2) time complexity
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
    

    