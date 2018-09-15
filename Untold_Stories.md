# Untold Stories of Pandas
Micheal Wu

## Can I change the data itself? How?

#### Modify the df of Pandas:

`df.drop('label')` will do nothing to `df`

We should:

`df = df.drop('label')` 

trivial but tricky right?

#### What about Numpy array?

(Numpy arrays are immutable)[https://docs.scipy.org/doc/numpy/reference/arrays.scalars.html].

Therefore, we must assign it to a new one:

`new_arr = np.delete(arr, [1, 3, 5])`

#### What about Python list?

Python lists are mutable.

The one line `list_a.extend([1, 2, 3])` will modify the python list `list_a`)
