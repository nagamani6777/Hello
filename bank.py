import sys
class Customer:
	bankname="statebank"
	def __init__(self,name,balence=0.0):
		self.name=name
		self.balence=balence
	def deposit(self,amt):
		self.balence=self.balence+amt
		print( 'balence after deposit:',self.balence)
	def withdraw(self,amt):
		if amt>self.balence:
			print('insufficient funds...can not perform the operation')
			sys.exit()
		self.balence=self.balence-amt
		print('balence after withdrawl:',self.balence)
	print('welcome to ',Customer.bankname)
	name=input('enter your name:')
	c=Customer(name)
	while True:
		print('d-Deposit\n w-withdraw\n e-exit')
		option=input('choose your option:').lower()
		if option=='d':
			amt=float(input('enter amount to deposit:'))
			c.deposit(amt)
		elif option=='w':
				amt=float(input('enter amount to withdraw:'))
				c.withdraw(amt)
		elif option=='e':
			print('thanks for banking')
			sys.exit()
		else:
			print('invalid option..plz choose a valid option')

			
 

    