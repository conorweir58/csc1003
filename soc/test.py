import math  
  
  
# function for finding roots  
def findRoots(a, b, c):  
  
    dis_form = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(dis_form))  
  
  
    if dis_form > 0:  
        print(" real and different roots ") 