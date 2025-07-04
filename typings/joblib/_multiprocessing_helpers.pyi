"""
This type stub file was generated by pyright.
"""

import multiprocessing as mp
from multiprocessing.context import assert_spawning

"""Helper module to factorize the conditional multiprocessing import logic

We use a distinct module to simplify import statements and avoid introducing
circular dependencies (for instance for the assert_spawning name).
"""
mp = ...
if mp:
    ...
if mp is not None:
    _rand = ...
if mp is not None:
    ...
else:
    assert_spawning = ...
