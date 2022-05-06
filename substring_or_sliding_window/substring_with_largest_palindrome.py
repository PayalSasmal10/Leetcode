# find the largest palindrome
strr = "defgabbcbba"
#o/p = abbcbba

class Palindrom:
    new_list = []
    def largestPalindrome(self, strr):
        for i in range(len(strr)):
            for j in range(i,len(strr)):
                self.new_list.append(strr[i:j+1])

        for k in self.new_list:
            if k == k[::-1]:
                pass



