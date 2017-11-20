'''Auto Generated Python file using COOL_Py translator.'''

from base import IO, Object, String, Integer, Boolean

class Main(IO):

    def out(self):
        block_var_0 = None
        self.out_string(String('2 is trivially prime.\n'), )
        block_var_0 = Integer(2)

        return block_var_0
    testee = out()
    stop = Integer(500)
    def m(self):
        conditional_var_0 = None
        while(Boolean(True)):
            block_var_1 = None
            self.testee = (self.testee) + (Integer(1))
            self.divisor = Integer(2)
            conditional_var_1 = None
            if_var_2 = None
            if((self.testee) < ((self.divisor) * (self.divisor))):
                if_var_2 = Boolean(False)
            else:
                if_var_3 = None
                if(((self.testee) - ((self.divisor) * ((self.testee) / (self.divisor)))) == (Integer(0))):
                    if_var_3 = Boolean(False)
                else:
                    if_var_3 = Boolean(True)
                if_var_2 = if_var_3
            conditional_var_1 = if_var_2
            while(conditional_var_1):
                self.divisor = (self.divisor) + (Integer(1))
                if_var_2 = None
                if((self.testee) < ((self.divisor) * (self.divisor))):
                    if_var_2 = Boolean(False)
                else:
                    if_var_3 = None
                    if(((self.testee) - ((self.divisor) * ((self.testee) / (self.divisor)))) == (Integer(0))):
                        if_var_3 = Boolean(False)
                    else:
                        if_var_3 = Boolean(True)
                    if_var_2 = if_var_3
                conditional_var_1 = if_var_2
            if_var_4 = None
            if((self.testee) < ((self.divisor) * (self.divisor))):
                block_var_2 = None
                self.out = self.testee
                self.out_int(self.out, )
                block_var_2 = ["self.out_string(String(' is prime.\\n'), )"]
                if_var_4 = block_var_2
            else:
                if_var_4 = Integer(0)
            if_var_5 = None
            if((self.stop) <= (self.testee)):
                if_var_5 = String('halt').abort()
            else:
                if_var_5 = String('continue')

        return block_var_1

    def main(self):
            self.out()
            self.m()
            return Integer(0)


if __name__ == '__main__':
    m = Main()
    m.main()
