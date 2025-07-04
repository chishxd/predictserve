"""
This type stub file was generated by pyright.
"""

from ._multiprocessing_helpers import mp
from .externals.loky import wrap_non_picklable_objects

"""
Small shim of loky's cloudpickle_wrapper to avoid failure when
multiprocessing is not available.
"""
if mp is not None:
    ...
else:
    wrap_non_picklable_objects = ...
__all__ = ["wrap_non_picklable_objects"]
