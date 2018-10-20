# Implementation of switch-case statement in Python
Full description & explanation: 

[https://zablo.net/blog/post/python-switch-case-statement](https://zablo.net/blog/post/python-switch-case-statement)

## Usage

### With simple objects
```python
with switch("yolo") as case:
    case("aosdk", 1)
    case("askdoska", 2)
    case("asodaodki", 3)
    case("yolo", 666)
    case("asdksoa", 4)
    result = case.result
print(result)
>>> 666
```

### With lambdas
```python
y = object()
with switch(y) as case:
    case(lambda: isinstance(y, str), "Some characters")
    case(lambda: isinstance(y, int), "Numberzzzz")
    case(lambda: isinstance(y, float), "Why u not double?")
    case.default(r"¯\_(ツ)_/¯")
    result = case.result
print(result)
>>> "¯\_(ツ)_/¯"
```

### With functions
```python
def one(x):
    return x == 1

def two(x):
    return x == 2

with switch(2) as case:
    case(one, 10)
    case(two, 20)
    result = case.result
print(result)
>>> 20
```