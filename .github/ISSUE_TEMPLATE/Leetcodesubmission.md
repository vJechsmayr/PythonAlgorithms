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
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        
        int n = matrix.size();
        for(int i=0;i<n;i++){
            for(int j=0;j<n-i;j++){
                swap(matrix[i][j],matrix[n-j-1][n-1-i]);
            }
        }
        reverse(matrix.begin(),matrix.end());
        
        
        
    }
};
```

## Link To The LeetCode Problem
[LeetCode](https://leetcode.com/problems/rotate-image/)
