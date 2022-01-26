def numIdenticalPairs(nums):
    countPairs = 0
    counter = {}
    
    for n in nums:
        print(counter)
        if n in counter:
           print("n:", n)
           countPairs += counter[n]
           print(countPairs)
           print("counter", counter[n])
           counter[n] += 1
           print("after adding:", counter[n])
        else:
           counter[n] = 1
           print("else counter", counter[n])
    return countPairs

print(numIdenticalPairs([1,2,3]))