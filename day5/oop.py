class Mobile:
	color = ''
	model = ''
	price = 0
		
	def __init__(self,color,model,price):
		self.color = color
		self.price = price
		self.model = model
			
	def show(self):
		print(f" {self.color} {self.price} {self.model}")

		

mobile1 = Mobile('white','S', 100);
mobile2 = Mobile('black', 'J', 50);

mobile1.show()
mobile2.show()





