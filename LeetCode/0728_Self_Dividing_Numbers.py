class Solution:
   def selfDividingNumbers(self, left: int, right: int) -> List[int]:
      ans = []
      for i in range(left,right+1):
         flag = False
         tempVal=i
         while tempVal:
               remainder = tempVal % 10
               if not remainder:
                  flag = True
                  break
               else:
                  if i % remainder:
                     flag = True
                     break
               tempVal //= 10
         if not flag:
            ans.append(i)
      return ans