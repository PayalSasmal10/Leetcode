# how many charecter presents in my strings

# from cv2 import add


# dictt = {'p':1, 'a': 2, 'y': 1, 'l': 1}
# j = 0
# dictt.update({'t': 8})
# dictt.in
# print(dictt)

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


