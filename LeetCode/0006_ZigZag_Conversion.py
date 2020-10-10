'''
## Description of the Problem

The string "PAYPALISHIRING" is written in a zigzag pattern
on a given number of rows like this:

(you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

## Example 1:
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

## Example 2:
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
```

## Explanation:

```
P     I    N
A   L S  I G
Y A   H R
P     I
```

## Example 3:

```
Input: s = "A", numRows = 1
Output: "A"
```

## Constraints:

- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000


## Link To The LeetCode Problem
[6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)
'''


class Solution:
    s = ''
    numRows = 1

    # transitionColumns is the number of extra columns needed to get the
    # text from the bottom row back to the top row
    def zigZagTransitionColumns(self) -> int:
        transitionColumns = self.numRows - 2
        if transitionColumns < 0:
            transitionColumns = 0
        return transitionColumns

    # patternColumns is the number of columns taken up by each full pattern
    # the first column is downward, and then we need columns for the upward
    def zigZagPatternColumns(self) -> int:
        return 1 + self.zigZagTransitionColumns()

    # patternSize is the number of elements in each repeated pattern
    def zigZagPatternLength(self) -> int:
        # there are numRows letters in the first column
        # followed by one letter per transitionColumn
        return self.numRows + self.zigZagTransitionColumns()

    # computes the number of total columns needed by this string
    def zigZagMatrixColumns(self) -> int:
        patternLength = self.zigZagPatternLength()
        fullPatternCount = len(self.s) // patternLength
        columns = self.zigZagPatternColumns() * fullPatternCount

        # how many extra letters are there?
        extraLetters = len(self.s) - (patternLength * fullPatternCount)
        if extraLetters > 0:
            columns += 1
        if extraLetters > self.numRows:
            columns += extraLetters - self.numRows
        return columns

    # converts the index of the input string to the address
    # in the output matrix
    def zigZagMatrixIndex(self, elementIndex: int) -> tuple:
        patternLength = self.zigZagPatternLength()

        # which pattern repetition holds this element (zero-based)
        patternOfElement = elementIndex // patternLength

        # where in the pattern repetition is this element
        indexInPattern = elementIndex % patternLength

        matrixRow = indexInPattern
        matrixColumn = patternOfElement * self.zigZagPatternColumns()
        bottomRowIndex = self.numRows - 1

        # correct the row and column numbers (remember these are zero-based)
        if indexInPattern > bottomRowIndex:
            extraColumns = indexInPattern - bottomRowIndex
            matrixColumn = matrixColumn + extraColumns

            # row decrements by 1 for each extra column
            matrixRow = bottomRowIndex - extraColumns

        # i, j
        return (matrixColumn, matrixRow)

    # creates a zigzag matrix
    def generateZigZagMatrix(self) -> list:
        matrix = []
        for i in range(self.zigZagMatrixColumns()):
            matrix.append([])
            for j in range(self.numRows):
                matrix[i].append('')
        for elementIndex, char in enumerate(self.s):
            i, j = self.zigZagMatrixIndex(elementIndex)
            matrix[i][j] = char
        return matrix

    # prints out the zigzag matrix
    def generateZigZagString(self, nullChar: str = ' ', lineEndings: str = '\n'):
        lines = []
        matrix = self.generateZigZagMatrix()
        for j in range(self.numRows):
            rowChars = []
            for i in range(self.zigZagMatrixColumns()):
                char = matrix[i][j]
                rowChars.append(char if char != '' else nullChar)
            lines.append(''.join(rowChars))
        return lineEndings.join(lines)

    def zigZagConversion(self, s: str, numRows: int, asMatrix: bool = False) -> str:
        '''
        The ZigZag format fills all available rows vertically in the first column,
        then, fills rows "diagonally" on the way back up to the top row of a subsequent
        column, and then repeats.

        The input string is the normal content.        
        '''
        self.s = s
        self.numRows = numRows
        if asMatrix:
            return self.generateZigZagString(nullChar=' ', lineEndings='\n')
        else:
            return self.generateZigZagString(nullChar='', lineEndings='')


# testing
if __name__ == '__main__':
    toConvert = 'PAYPALISHIRING'
    converter = Solution()
    for i in range(4):
        print(f'\nENCODING: {toConvert} with {i+1} rows')
        print('\n-- matrix -----------------')
        print(converter.zigZagConversion(toConvert, numRows=i+1, asMatrix=True))
        print('\n-- line -------------------')
        print(converter.zigZagConversion(toConvert, numRows=i+1, asMatrix=False))
        print()
