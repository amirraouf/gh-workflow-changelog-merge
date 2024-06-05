from incremental import getVersionString
from app._version import __version__

if __name__ == '__main__':
    print(getVersionString(__version__).split(" ")[1])