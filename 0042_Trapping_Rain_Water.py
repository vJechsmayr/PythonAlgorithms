class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n>0:
            left = [0]*n 
            right = [0]*n 
            result = 0

            # Fill left array 
            left[0] = height[0] 
            for i in range( 1, n): 
                left[i] = max(left[i-1], height[i]) 

            # Fill right array 
            right[n-1] = height[n-1] 
            for i in range(n-2, -1, -1): 
                right[i] = max(right[i + 1], height[i]); 

            for i in range(0, n): 
                result += min(left[i], right[i]) - height[i] 

            return result
        else:
            return 0