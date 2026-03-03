# Python Modulo Function with Unit Tests

Homework assignment for the course "Python Programmer from Scratch with ChatGPT 2.0".

**Module 12 — Automated Testing | Lesson AT01**

## Task

Implement a modulo(a, b) function that computes the remainder of division
and write unit tests covering both normal operation and zero-division error handling.

## Project Structure

```
python-unittest-modulo/
├── main.py    - modulo function implementation
└── test.py    - unittest test suite
```

## Implementation

```python
def modulo(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя")
    return a % b
```

## Tests

The test suite covers two scenarios:

- **test_modulo_success** — verifies correct remainder values using assertEqual
- **test_modulo_by_zero** — verifies ValueError is raised when b == 0 using assertRaises

## Running Tests

```bash
python -m unittest test -v
```

Expected output:

```
test_modulo_by_zero (test.TestModulo) ... ok
test_modulo_success (test.TestModulo) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Key Concepts Practiced

- unittest.TestCase — base class for test cases
- assertEqual(result, expected) — asserts two values are equal
- assertRaises(ExceptionType, func, *args) — asserts a function raises a given exception
- raise ValueError(...) — raising exceptions for invalid input

## Requirements

- Python 3.x (no third-party libraries required)
