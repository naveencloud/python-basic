"""String Formating
   {:fmt-str}
"""

from math import pi  ## we need to add only pi instead of math.pi

## if we import module only we need to define math.pi

def compute(radius):  # def is defining function keyword, function_name and with argumnet function returns a value it is dynamic
    return pi * radius ** 2 ## Return value to Function ,,,, Exponential Operator
    #function defination

try:    # If we define TRY and atleast 1 except need to be define otherwise its a syntax error
    user_radius = float(input('enter the radius :'))
    area = compute(user_radius) #function calling and "area" is a variable. user_radius is a argument which retun value
   # print("area :", area)
    #print("area : {:.3f}".format(area)) # Sring formate and round with 3 floating point. First Output will be formated with first argumnet and it value

    print("radius: {} \narea : {:.3f}".format(user_radius, area)) # it will give output of radius and area,

except ValueError as err:
    print(err)


