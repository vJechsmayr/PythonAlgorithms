import re

class Solution:
    def reorderSpaces(self, text: str) -> str:

        # Regular expression that matches a leading character, 1 or more spaces
        # and a trailing character
        regex = re.compile(r"(?<=[a-zA-Z])\s+(?=[a-zA-Z])")

        # Finding total number of individual space characters
        num_spaces = text.count(" ")

        # Counting how many gaps there are using the regex above
        num_gaps = len(re.findall(regex, text))


        spaces_per_gap = num_spaces // num_gaps
        end_spaces = num_spaces % num_gaps

        # Replacing the gaps with the calculated number of spaces
        text = re.sub(regex, " " * spaces_per_gap, text)

        # Removing leading and trailing spaces for the string
        text = text.strip()

        # Adding the final spaces
        text += (" " * end_spaces)

        return text
