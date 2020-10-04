class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        length = len(magazine)

        for index in range(len(ransomNote)):
            if ransomNote[index] in magazine:
                match = magazine.find(ransomNote[index])

                magazine = magazine[:match] + magazine[match + 1 :]
            else:
                return False
            if length - len(magazine) == len(ransomNote):
                return True
