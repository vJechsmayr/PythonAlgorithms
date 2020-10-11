class Solution(object):
    def replaceElements(self, arr):
        arr1 = []
        for i in range(len(arr)):
            if i==len(arr)-1:
                arr1.append(-1)
            else:
                arr1.append(max(arr[i+1:]))
        return arr1