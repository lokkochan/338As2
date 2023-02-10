import timeit
from matplotlib import pyplot as plt 
import pandas as pd 
def memoize(k): 
    list_memory = {}  
    def check_function(l): 
        if l not in list_memory: 
            list_memory[l] = k(l) 
        return list_memory[l] 
    return check_function
def fibonacci(n): 
      if (n<2): 
         return 1  
      return (fibonacci(n-1) + fibonacci(n-2))
fibonacci =memoize(fibonacci) 
print(fibonacci(100))
