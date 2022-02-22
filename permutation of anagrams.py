# how many ways my name can be on anagram

# from os import name


class Anagram:

    def __init__(self, name) -> None:
        self.name = name
        self.duplicate_values = ""

    def fact(self,n):
        if n == 0:
            return 1
        else:
            return n * self.fact(n-1)
    
    def fetch_duplicate(self):
        dictt = {}
        for i in range(len(self.name)):
            countt = 0
            if self.name[i] in dictt:
                dictt[self.name[i]] = dictt[self.name[i]] + 1
            else:
                dictt[self.name[i]] = countt + 1

        for i in dictt:
            if dictt[i] > 1:
               self.duplicate_values = dictt[i]
        self.anagram_way()

    def anagram_way(self):
        length = len(self.name)
        actual_length = self.fact(length)
        print(actual_length//self.fact(self.duplicate_values))


an = Anagram("Payal")
an.fetch_duplicate()
        