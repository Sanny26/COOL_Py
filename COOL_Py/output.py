'''Auto Generated Python file using COOL_Py translator.'''

from base import IO, Object, String, Integer, Boolean

class Cons(Object):

    def x_funct(self):
        if_var_0 = None
        if((Integer(2)) < (Integer(3))):
            if_var_0 = Integer(2)
        else:
            if_var_0 = Integer(3)
    
        return if_var_0
    
    def isNil(self, ):
            return Boolean(False)    
    
    def init(self, hd, tl, ):
            block_var_0 = None
            self.xcar = hd
            
            self.xcdr = tl
            
            block_var_0 = self
            return block_var_0    
    def main(self):
            self.xcar = None
            self.xcdr = None
            self.x = self.x_funct()
            return self


if __name__ == '__main__':
        m = Main()
        m.main()

