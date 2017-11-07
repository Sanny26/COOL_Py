class Cons():

  xcar = None
  xcdr = None
  def isNil(self, ) -> bool:
      return False  
  def init(self, hd : int,tl : list()) -> Cons:
      self.xcar = hd
      self.xcdr = tl
      xx = 10
      return self

if __name__ == "__main__":
	c = Cons()
	c.init(10, 25)
	print(c.xcar)
	print(c.xcdr)

	if 10 == 20:
		print('sdsds')

	else:
		print('wewewe')
