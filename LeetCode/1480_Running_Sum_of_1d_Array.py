class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answers=[]
        answers.append(nums[0])
        for i in range(1,len(nums)):
            answers.append(answers[-1]+nums[i])
        return answers