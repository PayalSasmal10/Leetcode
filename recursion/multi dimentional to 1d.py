"""
i/p: [[1], [1, 2, [3, 4, 5]], [6, [7, 8, [9, 10, 11], [12, 13]]]]
o/p: [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

"""



class A:
    res = []
    # def __init__(self) -> None:
    #     self.res = []
    def singleDimention(self,arr):
        for i in range(len(arr)):
            if isinstance(arr[i], list):
                self.singleDimention(arr[i])
            else:
                self.res.append(arr[i])
        return self.res

a = A
print(a.singleDimention([[1], [1, 2, [3, 4, 5]], [6, [7, 8, [9, 10, 11], [12, 13]]]]))
