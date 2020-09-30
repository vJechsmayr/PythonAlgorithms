def threeSum(self, nums):
    nums.sort()
    result = []
    for left in range(len(nums) - 2): # renamed this to left because this will always be the leftmost pointer in the triplet
        if left > 0 and nums[left] == nums[left - 1]: # this step makes sure that we do not have any duplicates in our result output
            continue 
        mid = left + 1 # renamed this to mid because this is the pointer that is between the left and right pointers
        right = len(nums) - 1
        while mid < right:
            curr_sum = nums[left] + nums[mid] + nums[right]
            if curr_sum < 0:
                mid += 1 
            elif curr_sum > 0:
                right -= 1
            else:
                result.append([nums[left], nums[mid], nums[right]])
                while mid < right and nums[mid] == nums[mid + 1]: # Another conditional for not calculating duplicates
                    mid += 1
                while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                    right -= 1
                mid += 1
                right -= 1
    return result