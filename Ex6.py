#Kirsty O'Brien
#ex5
#define function
def factorial(n):
    #create error if number entered is below 0 - if and else line
    if n > 0:
        #create number to keep the rolling total
        num1 = 1
        #actual function 
        while n >= 1:
            num1 = num1 * n
            n = n-1
        return num1    
    else: print("Number must be positive for factorial to work. Result of minus is:")


#test to see if function actually works using number 5 as an example
   

test = factorial(5)
print(test)
