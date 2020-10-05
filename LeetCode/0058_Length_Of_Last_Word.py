class Solution(object):
    def lengthOfLastWord(self, s):
        str = input("Input: ")
        list = str.split()
	if(len(list[-1])):
        	return len(list[-1])
	return 0