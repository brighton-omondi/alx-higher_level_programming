Sure! Let's explore Python's more data structures - Set and Dictionary.

## Set
A set is an unordered collection of unique elements. It is defined by enclosing elements within curly braces `{}` or by using the `set()` constructor.

### Creating a Set
```python
# Using curly braces
my_set = {1, 2, 3, 4, 5}

# Using set() constructor
another_set = set([5, 6, 7, 8, 9])
```

### Basic Operations on Sets
```python
# Adding elements to a set
my_set.add(6)

# Removing an element from a set
my_set.remove(3)  # Raises KeyError if the element is not present
my_set.discard(10)  # Removes the element if present, but does nothing if not present

# Union of two sets
union_set = my_set.union(another_set)  # or use the "|" operator

# Intersection of two sets
intersection_set = my_set.intersection(another_set)  # or use the "&" operator

# Difference between two sets
difference_set = my_set.difference(another_set)  # or use the "-" operator

# Check if a set is a subset of another set
is_subset = my_set.issubset(another_set)  # or use the "<=" operator

# Check if two sets have no elements in common (disjoint sets)
is_disjoint = my_set.isdisjoint(another_set)
```

## Dictionary
A dictionary is an unordered collection of key-value pairs. Each key must be unique and immutable (e.g., strings, numbers, or tuples). It is defined using curly braces `{}` with key-value pairs separated by a colon `:`.

### Creating a Dictionary
```python
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Using dict() constructor
another_dict = dict(name="Alice", age=25, city="London")
```

### Basic Operations on Dictionaries
```python
# Accessing elements using keys
name = my_dict["name"]
age = my_dict.get("age")  # Safely get a value with a default return value if key not found

# Modifying and adding elements
my_dict["city"] = "San Francisco"
my_dict["occupation"] = "Engineer"

# Removing elements from a dictionary
del my_dict["age"]  # Removes the key-value pair with the specified key
my_dict.pop("occupation")  # Removes and returns the value associated with the specified key

# Check if a key exists in the dictionary
if "name" in my_dict:
    print("Name exists!")

# Iterating through keys and values
for key in my_dict:
    print(key, my_dict[key])

# Using items() method to get key-value pairs directly
for key, value in my_dict.items():
    print(key, value)
```

Keep in mind that dictionaries do not guarantee the order of their elements (prior to Python 3.7, dictionaries were unordered). If you need ordered key-value pairs, consider using the `collections.OrderedDict` class from the `collections` module.