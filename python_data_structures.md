# Lists in python
* Lists in python are dynamic arrays.
* Class implements various common operations.
* Supports constant time indexing and assigning to index.
* Time complexity charts for the ops can be found at
https://wiki.python.org/moin/TimeComplexity
# Array Sequences
* Array sequence is general
* In python 3 main sequence classes
	1. List [1,2,3]
	2. Tuple (1,2,3)
	3. String "123"
* All support indexing e.g. t[0]=1
```python
mystring = 'abc'
print(mystring[0])
# a
```
* In `list_1.extend(list_2) ` *list_1* does not receive copies of *list_2*'s elements, only the references. 