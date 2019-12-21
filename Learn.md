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
