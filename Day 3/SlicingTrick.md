## Python Slicing

- *Slicing lists, tuples and dictionaries in python works like the for loop in C/C++*

	for example

	>**lis1 = [1, 2, 3, 4, 5, 6, 7]**
	
	list initialized

	>**lis1[x : y : z]**

	*Here*
	
	**x** ---> int i = some starting value, the initiation.

	**y** ---> i < or > some value, the termination condition.

	**z** ---> i ++ or -- or +=2 etc., the incement or decrement step.

- *lis1[x] means element of list **lis1** at index **x**.*
- *lis1[x: ] means all the elements of **lis1** after the index **x**, including **x**.*
- *lis1[ :y] means all elements of **lis1** before index **y**, not including **y**.*
- *lis1[ ::z], means all the elements in **lis1** from index 0 onwards with an increment step of **z**.*
	
	- ***if z is negative (-z), then the list traverses from index [max-1] to the start of list with a decrement step of z.***

>**print( lis1[2 : 6 : 2] )**

	>[3, 5]
