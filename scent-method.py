#!/usr/bin/env python
# coding: utf-8

# In[104]:


from sympy import *
# sympy using for solve equations

class equation:   
    
    def __init__(self):
        self.x , y , z = symbols("x y z")

        self.expr = None # cos(2*x) + x**2 
        self.exprDerivative = None 
            
    """take equation as input parameter"""
    def set_equation(self,expr):
        self.expr = expr
        
    """putting the values of x in equation(f(x)) find f(x)"""
    def f_of_x(self,value):

        temp = self.expr.subs(self.x,value)
        return temp 
    def derivative(self):
        self.exprDerivative = diff(self.expr)
        
    def f_derivative_x(self,value):
        self.exprDerivative = diff(self.expr)
        temp = self.exprDerivative.subs(self.x,value)
        return temp


class secant:
    def __init__(self):
        self.eq = equation()
        
        self.expr = None #230*x**4 + 18*x**3 + 9*x**2 - 221*x -9   
        
        self.tolerance = 10 # approximate upto 10th decimal places
        
        self.pnArray = [] #store previous secant values of pn

        self.fAarray = [] # store functions values given x

        
    """scent formula"""
    def pn(self,pn_0,pn_1,f_pn_0,f_pn_1):
        
        formula = round(float(pn_1 - ((f_pn_1)*(pn_1-pn_0) / (f_pn_1 - f_pn_0))),self.tolerance)
        
        return formula
    
    """approximate upto tolerance decimal places"""
    def approximates(self):
        
        for i in range(0,self.tolerance):
            
            pn_2 = self.pn(self.pnArray[i],self.pnArray[i+1],self.fAarray[i],self.fAarray[i+1])
            
            self.pnArray.append(pn_2)
            
            f_pn_2 = self.eq.f_of_x(pn_2)
            
            self.fAarray.append(f_pn_2)
            
            if ( self.pnArray[-1] == self.pnArray[-2]):
                break
                    
                
    def print_val(self):
        for i in self.pnArray:
            print("root approximation " , i)
            
    """taking inputs as parameters 1) expression or equation , interval pn0 and pn1 and tolerance"""
    def inputs(self,expr, pn0,pn1,tol):
        self.tolerance= tol
        self.expr = expr
        self.eq.set_equation(expr)
        
        self.pnArray.append(pn0)
        self.pnArray.append(pn1)
        
        self.fAarray.append(self.eq.f_of_x(pn0))
        self.fAarray.append(self.eq.f_of_x(pn1))
    
x , y , z = symbols("x y z")

expr = 230*x**4 + 18*x**3 + 9*x**2 - 221*x -9


sec = secant()
sec.inputs(expr, -1,0,10)
sec.approximates()
sec.print_val()
    
    


# In[102]:


class newton_raphson(equation):
    
    def __init__(self):
        
        self.x , y , z = symbols("x y z")
        self.pnArray = []
        self.tolerance = None
        self.fDerivativeN = None
        self.initialGuess = None
        
    def newton_formula(self,pn_1):
        
        fx = self.f_of_x(pn_1)
        
        fDx = self.f_derivative_x(pn_1)  
        
        pn = round((pn_1 - ((fx)/fDx)),self.tolerance)
        
        return pn
    
    def approximates(self):
        
        for i in range(0,21):
            pn = self.newton_formula(self.pnArray[-1])
            self.pnArray.append(pn)
            
            if self.pnArray[-1] == self.pnArray[-2]:
                break
        
    
    def inputs(self,expr,initialGuess, tol):
        self.tolerance = tol
        self.expr = expr
#         self.eq.set_equation(expr)
        
        self.pnArray.append(initialGuess)
    
    def print_val(self):
        for i in self.pnArray:
            print("root approximation " , i)
        

##############example 1######################
#this example may be stuck : limitation of newton raphson
x , y , z = symbols("x y z")

expr = x*3-x-3

nwt = newton_raphson()
initial_guess = 100
nwt.inputs(expr,initial_guess,10)
nwt.approximates()
nwt.print_val()

print()
##############example 2 ####################
x , y , z = symbols("x y z")

expr = x-cos(x)


nwt = newton_raphson()
nwt.inputs(expr, 0.785398,4)
nwt.approximates()

nwt.print_val()


# In[103]:


x , y , z = symbols("x y z")

expr = x-cos(x)


nwt = newton_raphson()
nwt.inputs(expr, 0.785398,4)
nwt.approximates()

nwt.print_val()


# In[ ]:





# In[ ]:





# In[96]:





# In[ ]:





# In[ ]:




