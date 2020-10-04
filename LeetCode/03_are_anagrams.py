import unittest

question_03 = """
An anagram I am

Given two strings s0 and s1, return whether they are anagrams of each other. Two words are anagrams when you can rearrange one to become the other. For example, “listen” and “silent” are anagrams.

Constraints:
- Length of s0 and s1 is at most 5000.

Example 1:

Input:
s0 = “listen”
s1 = “silent”

Output:
True

Example 2:

Input:
s0 = “bedroom”
s1 = “bathroom”

Output:
False
"""


# Implement the below function and run the program

def are_anagrams(word1, word2):
    a = sorted(word1)
    b = sorted(word2)
#Sort string alphabetically and return list
    word1 = "".join(a)
    word2 = "".join(b)
#Combine list elements into one string
    if (a==b):
        return True
    else:
        return False


class TestAreAnagrams(unittest.TestCase):

    def test_1(self):
        self.assertEqual(are_anagrams('listen', 'silent'), True)

    def test_2(self):
        self.assertEqual(are_anagrams('“bedroom”', 'bathroom'), False)

    def test_3(self):
        self.assertEqual(are_anagrams('madam', 'madam'), True)

    def test_4(self):
        self.assertEqual(are_anagrams('dabc', 'akbc'), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
