'''Auto Generated Python file using COOL_Py translator.'''

from base import IO, Object, String, Integer, Boolean

class Main(IO):

    
    def pal(self, s, ):
            if_var_0 = None
            if((s.length()) == (Integer(0))):
                if_var_0 = Boolean(True)
            else:
                if_var_1 = None
                if((s.length()) == (Integer(1))):
                    if_var_1 = Boolean(True)
                else:
                    if_var_2 = None
                    if((s.substr(Integer(0), Integer(1), )) == (s.substr((s.length()) - (Integer(1)), Integer(1), ))):
                        if_var_2 = self.pal(s.substr(Integer(1), (s.length()) - (Integer(2)), ), )
                    else:
                        if_var_2 = Boolean(False)
                    if_var_1 = if_var_2
                if_var_0 = if_var_1
            return if_var_0    
    i = None
    
    def main(self, ):
            block_var_0 = None
            self.i = ~(Integer(1))
            self.out_string(String('enter a string\n'), )            
            if_var_3 = None
            if(self.pal(self.in_string(), )):
                if_var_3 = self.out_string(String('that was a palindrome\n'), )
            else:
                if_var_3 = self.out_string(String('that was not a palindrome\n'), )
            return block_var_0    


if __name__ == '__main__':
    m = Main()
    m.main()

