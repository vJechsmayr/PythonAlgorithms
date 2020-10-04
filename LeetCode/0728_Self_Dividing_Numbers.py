class Solution:
   def selfDividingNumbers(self, left: int, right: int) -> List[int]:
      numbers = []
      for i in range(left, right + 1):
         temp = i
         while temp:
            remainder = temp % 10
            if remainder ==0 or i % remainder != 0:
               break
            temp //= 10
         else:
            numbers.append(i)
      return numbers
