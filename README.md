# Assignment 6

In this assignment, you will implement a complete heap-based priority queue.  In addition to the description of your task below, there is documentation in the file `heap.py` describing how each function you'll write should behave.

Your work for this assignment will be limited to the file `heap.py`.  In other files, you are provided with some additional starter code that defines the structures you'll be working with and prototypes functions you'll be using and writing.  *It's important that you don't modify the function prototypes.*  To help grade your assignment, we will use a set of unit tests that assume these functions exist and have the same prototypes that are defined in the starter code.  If you change the prototypes, it will cause the unit tests to break, and your grade for the assignment will likely suffer.  Feel free, however, to write any additional functions you need to accomplish the tasks described below.

## Implement a heap-based priority queue

Your task for this assignment is to implement a heap-based priority queue.  Specifically, in the file `heap.py`, you must define the heap and implement the following functions:

  * `__init__()` - allocates and initializes a heap-based priority queue. You can use a Python list
  * `__del__()` - frees all memory allocated to a heap
  * `is_empty()` - should tell the user whether a heap is empty
  * `insert()` - should insert an element with a specified priority value and data into a heap
  * `max()` - should return the *data* of the first element in a heap, maximum priority
  * `max_priority()` - should return the *priority* associated with the first element in a heap
  * `max_dequeue()` - should remove the first element from a heap and return its data
  * `_percolate_up()` - should percolate up (sift-up) the node until the max-heap property is met
  * `_percolate_down()` - should percolate down (sift-down) the node until the max-heap property is met

Here are some specific notes on how the priority queue you'll implement should behave:

  * Your priority queue must be implemented using a heap as the underlying data structure.

  * In the priority queue you implement, *higher* priority values (a.k.a. key(x)) should correspond to elements with higher priority.  In other words, the first element in the priority queue should be the one with the *highest* priority value among all elements in the collection.  For example, your priority queue should return an element with priority value 10 before it returns one with priority value 5.

  * Your `insert()` and `max_dequeue()` functions should both have average runtime complexity *O(log n)*, and your `max()` and `max_priority()` functions should both have average complexity *O(1)*.

## Testing your work

In addition to the starter code provided, you are also provided with some application code in `main.py` to help verify that your functions are behaving the way you want them to.  In particular, the code in `main.py` calls the functions you'll implement in this assignment, passing them appropriate arguments, and then prints the results.  You can use the provided `Makefile` to compile all of the code in the project together, and then you can run the testing code as follows:
```
python main.py
```
You can see some example output from a correct solution to the assignment in the file `example_output.txt`.

## Submission

As always, we'll be using Gradescope. Please submit your heap.py file through Gradescope. 

## Grading criteria

The assignment is worth 100 total points, broken down as follows:

* 5 points: `class definition` defines a heap-based priority queue using a python list
* 5 points: `__init__()` correctly allocates and initializes a heap-based priority queue
* 5 points: `__del__()` correctly frees all memory associated with a priority queue
* 5 points: `is_empty()` correctly determines whether a priority queue contains any elements or not
* 5 points: `max()` correctly returns the data of the element with the *highest* priority value
* 5 points: `max_priority()` correctly returns the *highest* priority value in a priority queue
* 20 points: `insert()` correctly inserts a value into a priority queue with the specified priority and restores the heap property as needed
* 20 points: `max_dequeue()` correctly removes the element with the *highest* priority from a priority queue and returns its value, restoring the heap property as needed
* 10 points: `insert()` and `max_dequeue()` are both *O(log n)*, and `max()` and `max_priority()` are both *O(1)*
* 20 points: assignment readme.txt file providing an explanation in your own words of what your code for each section listed above is doing. 


Note that we will only consider changes to `heap.py` when grading your work.  Changes to other files will be ignored.
