---
name: Rotate image
about: Use this Template to submit a new LeetCode Problem
title: 0048_Rotate_Image
labels: 'hacktoberfest'
assignees: 'grpnpraveen'

---

## Description of the Problem
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

## Code
```
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                if i != j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for each in matrix:
            each.reverse()
        return matrix
```

## Link To The LeetCode Problem
[LeetCode](https://leetcode.com/problems/rotate-image/)
