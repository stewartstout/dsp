# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

They are similar in that they are both indexed. Their primary difference is that tuples are immutable, whereas lists are not.

Dictionary keys must be immuatable, so only tuples will work.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Python sets contain only unique elements and are indexed, while lists can contain duplicate elements and are indexed. Because all elements in a set are hashable, searching for elements in a set is much faster than in a list. A possible exception is a situation in which the index of the element is known.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is used to create functions without a name. This can save time by eliminating the need to define functions.

Example:

avg_temps = [('portland',50),('boston',55),('new haven',57),('new york','60'),('cincinatti',59),('anchorage',15),('des moines',56)]
print sorted(avg_temps,key=lambda t:t[1])



---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions create new lists using existing ones. They transform an iterable input into new sequences with an optional filter. They are similar to for loops but can be written in a single line.

The example below illustrates the difference between a for loop and list comprehension using a simple example that prints the squares of even integers between 1 and 10.

For loop:

for i in range(10):
  if i % 2 == 0:
    print i*i
    
List comprehension:

squares_of_evens = [i*i for i in range(10) if i % 2 == 0]
print squares_of_evens

List comprehensions are also similar to a 'map' followed by a 'filter'.

For example, the list comprehension squares_of_evens above could be re-written as:

squares_of_evens = map(lambda n:n*n, filter(lambda n:n%2 == 0, range(10))

Though they accomplish the same task, list comprehensions are much faster than the 'map'/'filter' combination when a lambda is used.

Set comprehensions and dictionary comprehensions are very similar.

Below is an example of a set comprehension:

vowels_in_a_word = {l for l in 'example word' if l in 'aeiou'}

Dictionary comprehensions create keys and values from a list. Below is an example that returns even integers from 0 to 9 if those integers are even:

{x:x*x for x in range(10) if x%2 == 0}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





