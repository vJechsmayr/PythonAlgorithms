class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_list = [0]*(2*n)
        left_index = 0
        right_index = n
        for index in range(0, 2*n):
            if index%2 == 0:
                shuffled_list[index] = nums[left_index]
                left_index += 1
            else:
                shuffled_list[index] = nums[right_index]
                right_index += 1
        return shuffled_list
