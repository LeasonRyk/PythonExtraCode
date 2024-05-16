# PythonExtraCode
# Timing Context Manager

This Python script provides a timing context manager that measures the execution time of functions and code blocks.

## Installation

No installation is required. Simply copy the `timing_ctx` function into your Python project.

## How to Use

### Importing the Module

```python
import contextlib
import functools
import time
from typing import Callable, TypeVar, ParamSpec, Generator
```

## Defining the Timing Context Manager
The timing_ctx function is a context manager that measures the execution time of code blocks within its context.

```python
@contextlib.contextmanager
def timing_ctx(name: str) -> Generator[None, None, None]:
    t0 = time.monotonic()
    try:
        yield
    finally:
        t1 = time.monotonic()
        print(f'LOG: {name} took: {t1 - t0}')
```

## Example Usage
```python
@timing_ctx('g.timing')
def g(x: int) -> int:
    with timing_ctx('something.else'):
        time.sleep(.2)

    return x ** x

g(10)
