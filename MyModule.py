#MyModule

def divide(dividend, divisor):
    if divisor > 0:  
        return dividend / divisor
    else:
        return f"Divisor must be greator than 0. You specified {divisor}"
    
print("MyModule.py: ", __name__)

import libs.mylib