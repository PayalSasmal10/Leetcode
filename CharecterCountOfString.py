# how many charecter presents in my strings

str1 = "payal"
test = {}
countt = 0
for i,j in enumerate(str1):
    if str1[i] not in test:
        test[str1[i]] = countt + 1
    else:
        test[str1[i]] = test[str1[i]] + 1
    
    countt = 0

print(test)


