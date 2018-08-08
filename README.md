Lessons Learned TODOs
========

All global variables are stored in globals()
------------
  See https://stackoverflow.com/questions/3972872/python-variables-as-keys-to-dict
  
You can use a switch statement in python via a Dictionary
------------
```python
dict {'a' : method1(),
      'b' : method2()}
      
#Invokes method1()    
dict['a'] 
```

**Add-On**
>Dictionaries can also be iterated with a default value using get
```python
dict.get('c', print "This variable does not exist - please debug")
```

Object Oriented Programming
------------


**Inheriting a class**
class toInherit(Parent)
> Parent is the parent class that inherits all variables and methods

**Overriding Methods**
You can override methods just by using the same function name as the parent class

**Static Methods**
Inserting the **@staticmethod** property on top of a class makes it callable (Cannot be called within the same class)
Use Class.method inorder to do recurstion here
```python
    @staticmethod
    def method1(var1, var2):
        return var + var2
```

**{Un}Packing Varables**
Functions can be packed:
```python
def method1(var1, var2):
  return var + var2
  
numbers = [1, 5]
print method1(*numbers)
>>> 6
```

Functions can also be unpacked
```python
def method1(*many_numbers):
  return sum(many_numbers)
  
numbers = [1, 5, 2, 2, 1, 2]
print method1(numbers)
>>> 13
```



  
