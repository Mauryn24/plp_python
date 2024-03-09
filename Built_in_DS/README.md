# Python Built-in Data Structures

Python provides several built-in data structures that facilitate efficient manipulation and organization of data. This README provides a brief overview of these data structures along with their common use cases.

## 1. Lists

Lists are ordered, mutable collections of elements. They are defined using square brackets [] and can contain elements of different types.

```python
my_list = [1, 2, 3, 'hello', True]
```

Common operations:
- Access elements by index
- Append, insert, remove elements
- Concatenate lists
- Slice lists

## 2. Tuples

Tuples are ordered, immutable collections of elements. They are defined using parentheses () and can contain elements of different types.

```python
my_tuple = (1, 2, 3, 'hello', True)
```

Common operations:
- Access elements by index
- Unpack tuple
- Use as keys in dictionaries
- Return multiple values from functions

## 3. Sets

Sets are unordered collections of unique elements. They are defined using curly braces {} or the `set()` constructor.

```python
my_set = {1, 2, 3, 4, 5}
```

Common operations:
- Add, remove elements
- Perform set operations like union, intersection, difference
- Test for membership

## 4. Dictionaries

Dictionaries are unordered collections of key-value pairs. They are defined using curly braces {} and key-value pairs separated by colons (:).

```python
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

Common operations:
- Access value by key
- Modify, add, remove key-value pairs
- Iterate over keys, values, or items
- Check for existence of keys

## 5. Deque

Deque (double-ended queue) is a mutable sequence that supports adding and removing elements from both ends efficiently.

```python
from collections import deque

my_deque = deque([1, 2, 3, 4, 5])
```

Common operations:
- Append, appendleft, pop, popleft
- Rotate deque
- Access elements by index

## Conclusion

Python's built-in data structures offer versatile options for organizing and manipulating data efficiently. Choosing the right data structure depends on the specific requirements and constraints of your problem.
