class pointer:
	def __init__(self,x,y):
		self.x=y
		self.y=y
		

	def move_up(self,px):
		self.y+=px

	def movedown(self,px):
		self.x-=px
	def move_right(self,px):
		self.x+=px
	def move_left(self,px):
		self.y-=px		
	def pos(self):
		print(self.x,self.y)
	
			



p1=pointer(0,0)
p1.pos()
p1.move_up(5)
p1.pos()
p1.movedown(3)
p1.pos()
p1.move_left(3)
p1.pos()
p1.move_right(2)
p1.pos()
