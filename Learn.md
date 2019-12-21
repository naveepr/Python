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
  
### Control Flow Statements

#### if statement
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
 
 
 
 
 
 
 
 
 
