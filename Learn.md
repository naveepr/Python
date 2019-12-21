# Python Notes

## 1. Python Interpreter

 - #!/usr/bin/env python to be used in the first line.

## 2. Calculation

 ### Numbers
 - **" "** within this quotes treated as normal string.
 - **//** this is floor division
 - ** to calculate the power 3 ** 2 gives 3 power 2.
 - variable should always be defined before using.

 ### Strings
 - Double and single quotes are equivalent.
 - **print** produces a better readable output.
 - \ can be used to escape the double quotes.
 - The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes.
 - to print as a raw string do this --> **print(r'C:\naveen\name')**.
 - """...""" can be used to print multiple lines. 

```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```
 - **\+** can be used to concatenate strings.
 - **\*** can be used to mulitply it.
 - Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
 #### Slicing 
 - string is indexed from 0 and the last letter is index -1.
 - word[start:end] characters. Start is always included and the end excluded.
 - Indexes in a string are as shown.
  
   | 0,-3 | 1,-2 | 2,-1 |
   |------|------|------|
 
 - Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error. If you need a different string, you should create a new one.
 - **len()** returns the length of the string.
 
 ### Lists
 ```python
 squares = [1, 4, 9, 16, 25]
 ```
 - slicing can also be applied here.
 - All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list.
 - Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content.
 ```python
 >>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
 ```
 - It is possible to nest lists (create lists containing other lists):
 ```python
 >>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
 ```
  - There is no need to escape doulbe quote within single quote but not vice-versa.
  
## 3. Control Flow Statements

### if statement
```python
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
```

### for statement
```python
>>> for w in words:
...     print(w, len(w))
```
 
### range function
 ```python
 >>> for i in range(5):
...     print(i)
 ```
 - range(5,10) --> from 5 to 9
 - range(0,10,3) --> increments of 3
 - enumerate(iterable, start=0) 
```python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

>>> print(range(10))
range(0, 10)
```

### pass statement
- The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:
```python
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...

>>> class MyEmptyClass:
...     pass
...

>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```
### Functions
```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

- If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

- When a final formal parameter of the form \*\* name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form \*name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before \*\*name.) For example, if we define a function like this:
```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```

- A function definition may look like:
```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

- Any formal parameters which occur after the \* args parameter are \‘keyword-only\’ arguments, meaning that they can only be used as keywords rather than positional arguments.

- In the same fashion, dictionaries can deliver keyword arguments with the \*\*-operator:
```python
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]

>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

```

### Lambda Expression
```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43

>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```
## 4. Data Structures

### Lists
- list.append(x)
- list.extend(iterable)
>Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
- list.insert(i, x) 
>Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
- list.remove(x) 
>Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
- list.pop([i])
>Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
- list.clear()
>Remove all items from the list. Equivalent to del a[:].
- list.index(x[, start[, end]])
>Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item. The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
- list.count(x)
>Return the number of times x appears in the list.
- list.sort(key=None, reverse=False)
>Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
- list.reverse()
>Reverse the elements of the list in place.
- list.copy()
> Return a shallow copy of the list. Equivalent to a

- You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. 
- Using list as stack
```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

- Using list as queue
```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

- List Comprehensions - A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```
- del statement - del a[0], del a

### Tuples and Sequences
- Tuples are immutable and contains heterogeneous elements in them.
```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```
### Sets
- Unordered collection which does not contain duplicate and immutable.
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```
### Dictionary
- The keys in the dictionary should be immutable.
- Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, 
```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```
- The dict() constructor builds dictionaries directly from sequences of key-value pairs:
```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}

>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

#### Looping techniques
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave

>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe

>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```
