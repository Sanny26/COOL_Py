"""Basic COOL library implementations in Python."""
import re
import sys


class IO:
    """Class for Input/Output Operations."""

    def out_string(self, string):
        """Print the string."""
        print(string, end="")
        return self

    def out_int(self, integer):
        """Print an integer."""
        assert type(integer) is Integer or type(integer) is int
        print(integer, end="")
        return self

    def in_string(self):
        """Read string till new line."""
        x = input()
        return String(x)

    def in_int(self):
        """Read till new line, get first integer, discard everything else."""
        x = input()
        searchObj = re.search(r'([0-9]+).', x)
        if searchObj:
            return Integer(searchObj.group(1))
        else:
            raise TypeError("No integer given for call to <in_int>")


class Object:
    """Base Object class for COOL."""

    def abort(self):
        """Abort method."""
        sys.exit(0)

    def type_name(self):
        """Return the name of the Object class."""
        s = type(self).__str__
        return String(s)

    def copy(self):
        """Create a copy of the object."""
        return self


class String(str, Object):
    """Python string class, inheriting from Object."""

    def length(self):
        """Length of the string."""
        return len(self)

    def concat(self, s):
        """Concatenate."""
        return String(self + s)

    def substr(self, i, l):
        """Substring."""
        return String(self[i:i+l])


class Integer(int, Object):
    """Python integer class, inheriting from Object."""


class Boolean(Object):
    """Python boolean class, inheriting from Object."""

    def __init__(self, boolean):
        """Constructor."""
        self.bool = boolean

    def __nonzero__(self):
        """Boolean value for the object."""
        return self.bool

    def __bool__(self):
        """Boolean value for the object."""
        return self.bool
