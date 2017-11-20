'''Auto Generated Python file using COOL_Py translator.'''

from base import IO, Object, String, Integer, Boolean

class List(Object):


    def isNil(self, ):
            return Boolean(True)

    def isnotNil(self, ):
            return Boolean(False)

    def head(self, ):
            block_var_0 = None
            self.abort()
            block_var_0 = Integer(0)
            return block_var_0

    def tail(self, ):
            block_var_1 = None
            self.abort()
            block_var_1 = self
            return block_var_1

    def cons(self, i, ):
            return Cons().main().init(i, self, )
    def main(self):
            return self
class Cons(List):


    def isNil(self, ):
            return Boolean(False)

    def head(self, ):
            return self.car

    def tail(self, ):
            return self.cdr

    def init(self, i, rest, ):
            block_var_2 = None
            self.car = i

            self.cdr = rest

            block_var_2 = self
            return block_var_2
    def main(self):
            self.car = None
            self.cdr = None
            return self
class Main(IO):


    def print_list(self, l, ):
            if_var_0 = None
            if(l.isNil()):
                if_var_0 = self.out_string(String('\n'), )
            else:
                block_var_3 = None
                self.out_int(l.head(), )
                self.out_string(String(' '), )
                block_var_3 = self.print_list(l.tail(), )
                if_var_0 = block_var_3
            return if_var_0

    def main(self, ):
            self.mylist = None
            block_var_4 = None
            self.mylist = List().main().cons(Integer(1), ).cons(Integer(2), ).cons(Integer(3), ).cons(Integer(4), ).cons(Integer(5), )

            conditional_var_1 = None
            while(self.mylist.isNil()):
                block_var_5 = None
                self.print_list(self.mylist, )
                self.mylist = self.mylist.tail()

            return block_var_4


if __name__ == '__main__':
        m = Main()
        m.main()
