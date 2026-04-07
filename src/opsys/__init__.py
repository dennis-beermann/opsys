# Collect all elements to be exported globally, , so users can do
#     from proj import function
# instead of
#     from proj.module.component import function
from pyproj.module.component import function

__all__ = ["function"]
