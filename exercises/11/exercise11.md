# Exercise 11
*Swopnil N. Shrestha*
*CS-160*
*05/12/2018*

1. What is the result of the following expression written in reverse polish notation: `1 2 * 3 + 4 + 5 / 6 - 7 + 8 *`

```python
1 2 * 3 + 4 + 5 / 6 - 7 + 8 *
= 2 3 + 4 + 5 / 6 - 7 + 8 *
= 5 4 + 5 / 6 - 7 + 8 *
= 9 5 / 6 - 7 + 8 *
= 1.8 6 - 7  + 8 *
= -4.2 7 + 8 *
= 2.8  8 *
= 22.4
```

2. What is the Big-Oh time estimate of using Bubble sort on the following list `L = [1, 2, 4, 3, 5, 6, 7, 8, 9]`?

```python
O2(n)
```

3. Given the following list, `L = [1, 3, 5, 7, 9, 11, 13, 17, 19, 23]`, how many key comparisons the binary search algorithm would do when searching for the key 5?

*There would be three key comparisons:*
```python
11 == 5 (False)
5 < 11 (True)
5 == 5 (True)
(True)
```

4. Use the proper heapify approach to turn the following list into a min heap: [9, 8, 7, 6, 5, 4, 3, 2, 1]. Show each step and write the result as a list.

```python
	[9, 8, 7, 1, 5, 4, 3, 2, 6]
	[9, 8, 3, 1, 5, 4, 7, 2, 6]
	[9, 1, 3, 2, 5, 4, 7, 8, 6]
	[1, 2, 3, 6, 5, 4, 7, 8, 9]
```

5. Given the following set of keys, `L = [113, 117, 95, 106, 114, 108, 116, 105, 99]` show the resulting hash table assuming that you are using quadratic probing. Insert them in order from left to right and denote empty cells with None. The table holds exactly 16 keys. You do not need to worry about growing the table. Use a simple `(x % 16)` function on the keys.

```python
[None, 113, 114, 99, 116, 117, None, None, None, 105, 106, None, None, None, None, None, 108, None, None, 95]
```
