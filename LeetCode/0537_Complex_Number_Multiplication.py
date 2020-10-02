
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        x = a.split('+') 
        x[1] = x[1][:-1] 
        
        y = b.split("+") 
        y[1] = y[1][:-1] 
        
        a_real = int(x[0]) 
        a_img = int(x[1]) 
        
            
        b_real = int(y[0])     
        b_img = int(y[1]) 
        return str(a_real * b_real - a_img * b_img) + "+" + str(a_real * b_img + a_img * b_real) + "i"; 
        

