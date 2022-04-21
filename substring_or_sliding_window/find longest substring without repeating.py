
class Substring:
    def substringss(self,strings):
        
        for i in range(len(strings)):
            add_val = ""
            for j in range(i,len(strings)):
                if strings[j] in add_val:
                    for k in add_val:
                        if strings[j] == k:
                            add_val.translate({ord(k):None})
                            add_val += k
                else:
                    add_val += strings[j]

        return add_val
                    
                    

strings = "abcbbcca"

s = Substring()
print(s.substringss(strings))