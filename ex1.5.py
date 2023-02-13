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
def fibonacci2(n): 
      if (n<2): 
         return 1  
      return (fibonacci2(n-1) + fibonacci2(n-2))
list_optimize=[]
list_origninal=[]
for i in range(36):
    tm_op=timeit.timeit(lambda:fibonacci(i), number =1)
    list_optimize.append(tm_op)
    tm2_or=timeit.timeit(lambda:fibonacci2(i), number =1)
    list_origninal.append(tm2_or)
list_number=[]
for i in range (36):
    list_number.append(i)
print(list_optimize)
print(list_origninal)
fix, ax=plt.subplots()
ax.scatter(list_number,list_origninal,label="Original")
ax.scatter(list_number,list_optimize,label="Optimzed")
plt.legend()
plt.show()
