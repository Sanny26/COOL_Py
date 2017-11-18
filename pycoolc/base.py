"""IO Class Implementation in Python."""
import re
import sys

class IO:
    """Class for Input/Output Operations."""

    def out_string(self, string):
        """Print the string."""
        print(string)

    def out_int(self, integer):
        """Print an integer."""
        assert type(integer) is int
        print(integer)

    def in_string(self):
        """Read string till new line."""
        x = input()
        return x

    def in_int(self):
        """Read till new line, get first integer, discard everything else."""
        x = input()
        searchObj = re.search(r'([0-9]+).', x)
        if searchObj:
            return int(searchObj.group(1))
        else:
            raise TypeError("No integer given for call to <in_int>")

class Object:

    def abort(self):
        sys.exit(0)

    def type_name(self):
        s = type(self).__str__
        return s

    def copy(self):
        return self
