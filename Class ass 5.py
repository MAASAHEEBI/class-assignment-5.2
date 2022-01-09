##Write a Python class to implement pow(x, n)

x=int(input('enter base value: '))
n=int(input('enter power value: '))

class power_class:
    
    def pow(self, x, n) :            #define a function with base and power value
        
        if x==0 or x==1 or n==1:    # Checking the constraints on base and power   
            return x 

        if x==-1:                   #if base value is negative
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:                    #if power is equal to '0'
            return 1
        if n<0:                     #if power is negative
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
             return val*val
        return val*val*x

print(x,'to the power',n,'is =',power_class().pow(x, n))
