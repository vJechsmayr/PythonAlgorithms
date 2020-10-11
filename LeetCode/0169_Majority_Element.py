# this class will give us a solution
class Solution:

    # the function to find the majority element
    def majorityElement(self, arr):
        """
        finds the majority element in the arr
        :param arr: List[int] a list with elements
        :return: int , the majority element
        """

        # a dictionary of numbers we have seen
        seen_numbers = {}

        if len(arr) <= 2:
            return arr[0]

        # goes through the list of numbers and count the appearance amount
        for num in arr:
            # adds it to the dictionary
            if num not in seen_numbers:
                seen_numbers[num] = 1
            else:
                if (seen_numbers[num] + 1) >= (len(arr) / 2):
                    return num
                else:
                    # adds one to the counter
                    seen_numbers[num] += 1
