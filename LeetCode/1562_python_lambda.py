x = lambda a,b: a*b  
print("mul = ", x(20,10))  
<p><strong>Output:</strong></p>  
<div class="codeblock3"><pre>  
mul =  200  
</pre></div>  
<h2 class="h2">Why use lambda function?</h2>  
<p>The main role of the lambda function is better described in the scenarios when we use them anonymously inside another function. In Python, the lambda function can be used as an argument to the <strong>higher-order functions</strong> which accepts other functions as arguments.</p>  
<p>Consider the following example:</p>  
<h3 class="h3">Example 1:</h3>  
<div class="codeblock"><textarea name="code" class="python">  
#the function table(n) prints the table of n    
def table(n):    
    return lambda a:a*n # a will contain the iteration variable i and a multiple of n is returned at each function call    
n = int(input("Enter the number:"))    
b = table(n) #the entered number is passed into the function table. b will contain a lambda function which is called again and again with the iteration variable i    
for i in range(1,11):    
    print(n,"X",i,"=",b(i)) #the lambda function b is called with the iteration variable i  
