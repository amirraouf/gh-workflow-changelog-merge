"""
Provides app version information.
"""

# This file is auto-generated! Do not edit!
# Use `python -m incremental.update app` to change this file.

from incremental import Version, getVersionString

__version__ = Version("app", 0, 95, 0)
__all__ = ["__version__"]

if __name__ == '__main__':
    print(getVersionString(__version__).split(" ")[1])