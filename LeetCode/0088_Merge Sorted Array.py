class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        ##Method1
        i=0
        while(i<len(nums2)):
            # k = len(nums1)-m-len(nums2)
            # print(k)
            nums1[m+i] = nums2[i]
            # m -=1
            i+=1
        nums1.sort()
        
        ##Method2
#         totalLen = n+m
#         for k in nums2:
#             pos = m
#             j = 0
#             while(j<len(nums1)):
                
#                 if(nums1[j]>k):
#                     pos = j
#                     break
#                 j+=1
#             nums1.insert (pos,k)
#             m+=1
#             for x in range(0,len(nums1)-totalLen):
#                 del nums1[-1]
#             # print(nums1)

        