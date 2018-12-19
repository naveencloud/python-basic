# This -- Keyword in OOPS Clanguage. In Python we dont have

# Slef will be used to reference the current object/argument

# Every Instance argument of the Object is Self which are all pre defined. This are all Magic Operators
# In Runtime Python passes the Object reference to 'self' to process



class Demo:
    def __init__(self):
        print(self, 'am in constructor') # Its magic method which helps to create object

    def __del__(self):
        print(self, 'getting destroyed') # Its magic method which helps to cleanup object

d = Demo()
print(d)

