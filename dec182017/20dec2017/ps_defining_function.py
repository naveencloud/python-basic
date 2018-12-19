# Defining and building Function
# Fixed aka Positional arguments function and Default arguments
# Function is a resuable function

def power(x, y):
    return x ** y

print(power(3,4))

# Variable Argument Function

def demo(*args):  #args is always Tuple
    print(args)
    print(type(args))


demo()
demo(1,2,3,)
demo(1234)

##############################################

def demo(*args):  #args is always Tuple
    print(args)

items = [1,2,3,4,'v']
demo(items)
demo(*items) # Content of the Sequence of the Arguments