import contextlib
import functools
import time
from typing import Callable, TypeVar, ParamSpec, Generator

@contextlib.contextmanager
def timing_ctx(name: str) -> Generator[None, None, None]:
    t0 = time.monotonic()
    try:
        yield
    finally:
        t1 = time.monotonic()
        print(f'LOG: {name} took: {t1 - t0}')


@timing_ctx('g.timing')
def g(x: int) -> int:
    with timing_ctx('something.else'):
        time.sleep(.2)

    return x ** x

g(10)
