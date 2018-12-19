# Into to OOPS

# Default Name Space, While Importing Module has its own namespace. It is precidense with __moduleName__

import os
import math

class Demo:
    pass

d = Demo()
print(d)
print(Demo)
print(__name__)  # Default Name Space, While Importing Module has its own namespace. It is precidense with __moduleName__
print()
print(os.__name__)
print(math.__name__) # To check Namespace of Module

# To get the Reference of