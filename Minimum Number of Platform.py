"""
Q2- Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits. 
We are given two arrays that represent the arrival and departure times of trains that stop.
Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00} 
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00} 
Output: 3 
Input: arr[] = {9:00, 9:10} 
dep[] = {9:10, 12:00} 
Output: 2
"""

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200,1120,1130, 1900, 2000]
i = 1
j = 0
max_platform=needed_platform= 1
dep.sort()
arr.sort()
while(i < len(arr)):
    if arr[i] > dep[j]:
        j += 1
        max_platform -= 1
    else:
        max_platform += 1
        i += 1
    
    if max_platform>needed_platform:
        needed_platform = max_platform

print(needed_platform)




