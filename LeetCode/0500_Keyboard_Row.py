class Solution:

    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        is_in_row = lambda word, row: all(letter in row for letter in set(word.lower()))
        return [word for word in words if any(is_in_row(word, row) for row in rows)]
