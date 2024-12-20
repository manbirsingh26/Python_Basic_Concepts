"""
We can import and use one module in another module by using import keyword as below:
import module_name as alias_name

After importing a module we can use all the functions and methods of it.
"""

import mymodule as my
# We can also import a  single thing(s) from a module
#from mymodule import Student1
#from mymodule import Student2
print(my.Student1)
print(my.Student2)
print(my.Student3)
my.output()
print(dir(my)) 
#This dir() function provides the name of all the methods/functions and attributes contained inside the module
