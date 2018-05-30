---
layout: post
title:  "Deciphering Python Dictionaries and Lists - Part 1"
date:   2018-05-29 22:59:33 -0700
categories: Programming
tags: Programming Python
---
In an effort to retain my programming skills while I learn the ins-and-outs of Penetration Testing, I've decided to dive into the world of python programming past the basic scripting level. I've always loved the idea of one-liners and the little neat tricks when it comes to programming. Humble Bundle recently had a bundle called [Python Development Books](https://www.humblebundle.com/software/python-dev-kit-bundle) that had the book [Python Tricks: A Buffet of Awesome Python Features](https://www.amazon.com/Python-Tricks-Buffet-Awesome-Features/dp/1775093301). Before we get into the of some the neat dictionary trick I learned, let's start from the beginning.

In the Beginning
---------------------
When we first start to learn python programming, one of the first things we come across are lists and dictionaries. A list, being a simple list of data such as numbers and strings. A dictionary, being a list of key:value tuples. A list is initialized via the square bracket - **[]**, and a dictionary is initialized with the curly brackets **{}**.

```python
>>> list_x = [1,2,3,4,5]
>>> dict_y = {'a': 1, 'b': 2}
>>> list_x
[1,2,3,4,5]
>>> dict_y
{'a': 1, 'b': 2}
``` 

Both dictionaries and lists can be appended, deleted, counted, and modified whether its through the **list.remove(n)**, **list.pop()** or **del dict['key']**...etc. The main difference between the two is that dictionaries contain key:value pairs, and lists contain single pieces of data. Lastly, one important attribute of ditionaries is that dictionaries can only have one unique key, while lists can have as many duplicate values as it wants.

Dictionary Examples
```python
#Initializes dictionary
my_dict = {'a': 1, 'b': 2}
#Adds the folowwing key:value pair - 'new':'this will add a new key called new'
my_dict['new'] = 'this will add a new key called new'
#Changes the value of key 'a' to "this will change "a" to this value"
my_dict['a'] = 'this will change "a" to this value'
#deletes key 'b'
del my_dict['b']
#prints
for key, value in my_dict.items():
    print('\nKey: %s' % key)
    print('Value: %s' % value)
for key in my_dict.keys():
  print("This will iterate through keys and print the its value: %s." % my_dict[key])
my_dict2= {'c': 5, 'a': 2}
#Updates my_dict with my_dict2 overwriting values if keys are the same
my_dict.update(my_dict2)
```

List Examples
```python
my_list = [1,2,3,4,5]
#deletes last item
my_list.pop
#appends new item to list
my_list.append('new value')
#removes 4th item in the list
my_list.remove(3)
#clears list - Python 3 Only
my_list.clear()
```

Introducing Comprehensions
---------------------

As I read through some of the material in [Python Tricks: A Buffet of Awesome Python Features](https://www.amazon.com/Python-Tricks-Buffet-Awesome-Features/dp/1775093301), one of the things that came across my reading is the Python Enhancement Proposals - PEP for short. For those of you that don't know what PEPs are, in short they are community enhancement proposals by the Python community. Anyone can submit an idea for a new feature or process at [https://bugs.python.org](https://bugs.python.org), which will then go through a review proccess prior to approval. Additional information on PEPs can be found at [https://www.python.org/dev/peps/pep-0001](https://www.python.org/dev/peps/pep-0001).

Around 2000 and 2001 the idea that comprehensions should be created through these PEPs. Why? My guess is that initiating long lists and dictionaries was super tedious. Before comprehensions if you wanted to create a list of 1000+ items, you would either have to manually code a *for* loop OR manually insert each one to simply initiate a list.

```python
#List Initalizations prior to comprehensions
my_list = [1,2,3,4,5]
my_list.append(6)
my_list.append(7)
my_list.append(8)
my_list.append(9)
my_list.append(10)
#... OR
my_list2 = [1,2,3,4,5]
for x in range(6,1000)
  my_list2.append(x)
```

This was also the same case for dictionaries:
```python
#Dictionary Initalizations prior to comprehensions
my_dict = {'1': 1, '2': 4}
my_dict['3'] = 9
my_dict['4'] = 16
my_dict['5'] = 25
my_dict['6'] = 36
my_dict['7'] = 49
my_dict['8'] = 64
#... OR
my_dict2 = {'1': 1, '2': 4}
for x in range(3,1000):
  my_dict2[str(x)] = x*x
```

Can you see how this can get annoying? Who would want to initialize a completly seperate function that would bloat your code just to initialize a list/dictionary? No one, so the community created [PEP 202](https://www.python.org/dev/peps/pep-0202/), and shortly after [PEP 274](https://www.python.org/dev/peps/pep-0274/)

**PEP202:**
> It is proposed to allow conditional construction of list literals using for and if clauses. They would nest in the same way for loops and if statements nest now.

**PEP274:**
> PEP 202 introduces a syntactical extension to Python called the "list comprehension". This PEP proposes a similar syntactical extension called the "dictionary comprehension" or "dict comprehension" for short. You can use dict comprehensions in ways very similar to list comprehensions, except that they produce Python dictionary objects instead of list objects.

With the addition of PEP202, the  syntax for using list comprehensions is as follows:
```python
my_list = [x,y,z for x in list-x for y list-y for z in list-z... if [x,y,z...conditonal]]
```

Make sure to note the variables defined prior to the for loop. In short, this allows us to use a for loop to automate the creation of our lists. The list initialization code from the beginning would easily become:
```python
my_list = [x for x in range(1,1000)]
```

If want only even numbers we can do this:
```python
my_list = [x for x in range(1,1000) if x%2 == 0]
```

The syntax for Dictionary Comphrensions are similar except that this time you add a colon for your key:value pair. The dictionary code from the beginning would become:

```python
my_dict = {i : i*i for i in range(1000)}
```

A common usage for this is creating a dictionary of characters and their corresponding position. For example {'A': 1, 'B': 2...}. A one liner to initate such a dictionary is: 
```python
#Note this is 65+i because this converts the ASCII base 10 value to its correponding ASCII value
alpha_dict = {chr(65+i): i  for i in range(26}
```

This is a common way to initialize list and dictionaries that won't bloat your code. Remember to use it, and help the world create cleander code. I'll be posting in the next blog about Key-Value Arguments and Packing/Unpacking generalizations and their usefulness with Dictionaries.