class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        a_length = len(A)
        largest_left_index = 0
        largest_left = A[0]
        for i in range(2, a_length + 1):
            i *= -1
            if A[i] > A[i + 1]:
                largest_left_index = i
                largest_left = A[i]
                break
        
        largest_right_index = 0
        largest_right = 0
        for i in range(a_length + largest_left_index + 1, a_length):
            if A[i] > largest_right and A[i] < largest_left:
                largest_right_index = i
                largest_right = A[i]
        
        A[largest_left_index], A[largest_right_index] = A[largest_right_index], A[largest_left_index]
        return A
