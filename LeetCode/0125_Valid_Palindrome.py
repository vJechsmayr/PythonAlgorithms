class Solution:
    def isPalindrome(self, s: str) -> bool:
      alphnum = ""
      #Extract only alphanumeric characters from the given string
      for i in s:
         #Check whether the character is a lowercase letter or a number
         if ord(i)>=ord('a') and ord(i)<=ord('z') or ord(i)>=ord("0") and ord(i)<=ord("9"):
            alphnum+=i
         #Check whether the character is an uppercase letter. 
         #If yes,convert to lower case
         elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
            i = chr(32+ord(i))
            alphnum+=i
      #Reverse the alphanumeric string and check whether it is a palindrome
      rev= alphnum[::-1]
      result= rev==alphnum
      return result
        