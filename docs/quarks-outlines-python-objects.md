![Quark's Outlines: Python Objects](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jsj41kmzjth93iwse1mf.png)

# Quark's Outlines: Python Objects

*Overview, Historical Timeline, Problems & Solutions*

## An Overview of Python Objects

### What is a Python object?

In Python, all data is made of objects. A number is an object. A string is an object. A list is an object. Even functions and classes are objects. Python treats everything as an object so it can store, copy, or link all parts of a program.

When you run a program, you give Python values. Python turns those values into objects. The object holds data and also knows what it can do. This is what makes Python flexible and powerful.

**Python lets you represent all data as objects.**

```python
name = "Ada"
age = 36
```

Each value here becomes an object. The word `name` points to a string object. The word `age` points to a number object.

---

### What special properties do Python Objects have?
Every object in Python has three parts: identity, type, and value.  
- The **identity** is like a tag number. It never changes.  
- The **type** tells what the object can do. It also never changes.  
- The **value** is the actual content. It may or may not change, depending on the object’s type.

---

**Python objects have identity, type, and value.**

![Python objects have identity, type, and value.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jjsh3jf2r7tl6y7s8luv.png)



---


**Python lets you check identity, type, and value of any object.**

```python
a = "hello"
print(id(a))        # identity
print(type(a))      # type
print(a == "hello") # value
```

The `id()` function shows identity. The `type()` function shows the kind. The `==` operator compares value.

---

### What does mutability mean in Python?

Some Python objects can change. These are **mutable**. Lists, dictionaries, and sets are mutable. Others cannot change. These are **immutable**. Strings, numbers, and tuples are immutable.

You cannot change an immutable object. You can only make a new one. For mutable objects, you can change the content without changing the object’s identity.

---

**Python objects can be mutable or immutable.**


![Python objects can be mutable or immutable.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uid10haauv8z4cxq5fom.png)


---

**Python lets you change some objects and keeps others fixed.**

```python
x = [1, 2, 3]
x.append(4)    # changes x

y = "hello"
z = y.upper()  # creates new object
```

Here, `x` is mutable and changes in place. `y` is immutable, so `z` is a new object.

---

### How does Python destroy objects?

Python uses **garbage collection**. When nothing points to an object anymore, Python may remove it to free memory. But Python does not promise when this happens.


**Python garbage collection destroys objects with no references.**


![Python garbage collection destroys objects with no references.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1ridj8sfr79st92j4bn4.png)



---

If an object holds outside things, like a file or a window, the object should be closed on purpose. You do this with a `close()` method or `try...finally`.

**Python lets you clean up with `try...finally` or `close()`.**

```python
file = open("data.txt")
try:
    data = file.read()
finally:
    file.close()
```

Even if an error happens, `finally` makes sure the file is closed.

---

### What are containers in Python?

Some objects hold other objects. These are called **containers**. A list holds items. A dictionary holds key-value pairs. A tuple holds fixed values.

The value of a container depends on the value of what it holds. If the container holds mutable items, then the container’s value can seem to change, even if the container itself is immutable.

---

**Python lets you build complex structures with containers.**

```python
a = ([], [])   # tuple is immutable
a[0].append(1) # but item inside can change
print(a)
```

This shows that an immutable container like a tuple can hold a mutable list whose content changes.

---

## A Historical Timeline of Python Objects  
**Where do Python’s object rules come from?**

The Python object model combines ideas from memory design, computer languages, and real-world storage. This timeline shows how object behavior and features were shaped.

---

### People built memory-based computing models

**1945 — Von Neumann architecture** Defined programs and data in shared memory, influencing how identity and storage interact.  
**1958 — FORTRAN variables** Stored typed values in memory by name, starting the model of identity and value.  

---


### People invented object-based computing.

**1970 — Object-oriented idea**, Simula and Smalltalk, showed how code and data could live together.  
**1980 — ABC language**, used value-based types and readable structure, shaped Python’s model.  
**1983 — Reference counting**, used in CPython to track how many things point to an object.

---

### People designed Python’s object core

**1991 — Object model in Python 0.9.0** Introduced everything-as-an-object model, including identity, type, and value for all data.  
**2000 — Immutable type model** Python 2.0 defined fixed type rules and consistent mutability per type.  

---

### People refined garbage and containers

**2001 — Reference counting explained** Python 2.1 documented how reference counts drive cleanup.  
**2005 — Cycles and `gc` module** Python added features to detect cycles in memory that reference counting missed.  
**2012 — Context managers expanded** Python 3.1 and later improved `with` blocks and cleanup control for objects.  

---

### People made object identity more abstract

**2015 — Identity caching observed** Python 3.x began sharing values for small integers and strings to reduce memory use.  
**2025 — Type behavior clarified** Python core clarified that all behavior is tied to object type, not just value.

---

## Problems & Solutions with Python Objects

**How do Python objects help you model programs?**

Python objects make it easy to label, reuse, and manage all program values. These problems show how identity, type, and mutability work in real programs.

---

### Problem 1: Checking if two names point to the same thing

**Problem:** You want to know if two names refer to the same object, not just the same value.

**Solution:** Use the `is` operator. It returns `True` if two names point to the same object.

**Python lets you compare identity with `is`.**

```python
a = []
b = []
print(a is b)    # False

c = a
print(a is c)    # True
```

This shows `b` is a new object, even if its value is the same.

---

### Problem 2: Knowing if a value can change

**Problem:** You want to track whether something can be updated after it's made.

**Solution:** Learn which types are mutable. Strings, numbers, and tuples are not.

**Python lets you use immutable types for safety.**

```python
name = "Ada"
name[0] = "E"  # error: string is immutable
```

You must make a new string instead.

---

### Problem 3: Freeing external resources

**Problem:** You open a file or network link and want to make sure it gets closed, no matter what.

**Solution:** Use `try...finally` or `with` to manage cleanup safely.

**Python lets you ensure cleanup even after errors.**

```python
with open("log.txt") as f:
    lines = f.readlines()
```

The file closes itself when the block ends.

---

### Problem 4: Tracking type of an unknown object

**Problem:** You receive a value and need to know what kind of object it is.

**Solution:** Use the `type()` function to check.

**Python lets you check the kind of any object.**

```python
value = [1, 2, 3]
print(type(value))  # <class 'list'>
```

You can use this in debugging or condition checks.

---

### Problem 5: Handling containers with mutable contents

**Problem:** You make a tuple of lists. The tuple should be fixed, but the lists can change.

**Solution:** Understand that mutability of contained items still applies.

**Python lets mutable values live inside immutable containers.**

```python
a = ([],)
a[0].append(42)
print(a)  # ( [42], )
```

The tuple’s structure stays fixed, but its items can change.

---

## Like, Comment, Share, and Subscribe

Did you find this helpful? Let me know by clicking the like button below. I'd love to hear your thoughts in the comments, too! If you want to see more content like this, don't forget to subscribe to my channel. Thanks for reading!

---

[**Mike Vincent**](https://mike-vincent.carrd.co) is an American software engineer and writer based in Los Angeles. [More about Mike Vincent](https://mike-vincent.carrd.co)
