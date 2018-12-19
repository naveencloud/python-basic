# Processing Excel

import pyexcel
from collections import OrderedDict

content = {
    'names' : ['sam', 'pam', 'tim', 'naveen'],
    'age' : [34, 12, 22, 18],
    'gender' : ['male', 'femal', 'male', 'male']

}

# Below is to Order the content in dictionary
content1 = OrderedDict()
content1['names'] = ['sam', 'pam', 'tim', 'naveen']
content1['age'] = [3, 2, 1, 6]
content1['gender'] = ['male', 'female', 'male']

sh = pyexcel.get_sheet(adict= content)
sh.save_as('person1.xlsx')