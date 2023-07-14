from sympy import symbols, diff
import numpy as np

# q = int(input("Type your quantity of gas that you want to fil: "))
# p = int(input("Type gas price: "))

from sympy import symbols, diff

class GasPrice:
    def state_1(self, q, p):
        x = symbols('x')
        cost1 = q * x
        derivative_1 = diff(cost1, x).subs(x, p)
        print(f"The derivative of cost1 is {derivative_1}")
        return cost1.subs(x, p)
    
    def state_2(self, q, p, m, d):
        x = symbols('x')
        cost2 = q * x * (x - q * x) + m * d
        derivative_2 = diff(cost2, x).subs(x, p)
        print(f"The derivative of cost2 is {derivative_2}")
        return cost2.subs(x, p)

q1 = GasPrice()
print(q1.state_2(3, 4, 2, 1))