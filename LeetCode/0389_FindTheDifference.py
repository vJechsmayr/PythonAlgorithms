import sys
import random

# The function which will do the main operation of finding the difference

class Solution:
    def FindTheDifference(self, s: str, t: str) -> str:
        for char in s:
            if 96 <= ord(char) <= 123:
                if 0 < len(s) < 1000:
                    if len(t) == len(s) + 1:
                        extra_char = t[-1]
                        return extra_char
                    else:
                        print("Differnce between second and first string is more than 1")
        if s == '':
            if 0 <= len(s) <= 1000:
                if len(t) == len(s) + 1:
                    extra_char = t[-1]
                    return extra_char
                else:
                    print("Differnce between second and first string is more than 1")

if __name__ == "__main__":
    # Initialising the string variable with input from the user
    s = sys.argv[1]
    # Initialising the second string variable with input from user 
    t = sys.argv[2]
    solution = Solution().FindTheDifference(s, t)
    print(solution)