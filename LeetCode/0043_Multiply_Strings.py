class Solution:
    def multiply(self, num1: str, num2: str) -> str:
    	'''
    	Note: You must not use any built-in BigInteger library or convert the inputs to integer directly
    	'''
        l1 = len(num1)
        l2 = len(num2)
        
        x = 0
        for char in num1:
            l1 -= 1
            x += self.str_to_int(char, l1)
            
        y = 0
        for char in num2:
            l2 -= 1
            y += self.str_to_int(char, l2)
            
        xy = x * y
        
        return str(xy)
    
          
    def str_to_int(self, s, no_zeros):
        if s == '0':
            x = 0
        elif s == '1':
            x = 1
        elif s == '2':
            x = 2
        elif s == '3':
            x = 3
        elif s == '4':
            x = 4
        elif s == '5':
            x = 5
        elif s == '6':
            x = 6
        elif s == '7':
            x = 7
        elif s == '8':
            x = 8
        elif s == '9':
            x = 9
        return x * pow(10, no_zeros) 