#A person should be able to see what is available in teh supermarket inclusive of prices eg milk 44
#customer should be able to shop for items and get a bill at the end
#customer should be prompted to pay an amount collected by the cashier
#integrate with level 1 to return proper denominations
#WE HAVE A LOOP HOLE IN THE CODE BELOW....NOT REALLY A BUG BUT A USER CAN CHECKOUT AN EMPTY CART...NOTHING TOO SERIOUS
from app import CashierChange

class Shop():
	"""docstring for Shop"""
	def __init__(self):
		super(Shop, self).__init__()
		self.setUpInventory()

	def setUpInventory(self):
		self.shopInventory = {"Milk":44, "Honey":162, "Eggs":357, "Bread":41, "Spinach":42, "Towel":236, "Soda":65}
		# print(self.shopInventory);
		self.usershoppingCart = {}
		self.actionHandler()

	def actionHandler(self):
		self.actionUser = input("Welcome to Android 254 Shop. To preview our items press 1: To Shop for items press 2:")
		# we assume that you will actually pass an integer
		if(int(self.actionUser) == 1):
			self.previewInventory()
		elif(int(self.actionUser) == 2):
			self.doShopping()

	def previewInventory(self):
		for key in self.shopInventory:
			print("{} {}".format(key, self.shopInventory.get(key)))
		#to prevent program from closing...call the action handler to prompt the next step
		self.actionHandler()

	def doShopping(self):
		self.addToCart = input("To add item to cart simply type the item's name and press Enter to continue: ")
		self.itemState = False
		for key in self.shopInventory:
			# print(key.lower())
			if( self.addToCart.lower() in key.lower()):
				self.itemState = True
				#now add item to cart
				self.addToCartFunctionality(key)
		
		if(self.itemState == False):
			self.proceedTo = input("Item does not exist. Press 1 to try again or 2 to go home or quit to quit shopping: ")
			# remember to update this code
			if(int(self.proceedTo) == 1):
				self.doShopping()
			elif(int(self.proceedTo) == 2):
				self.actionHandler()
			else:
				self.quitShopping()

	def quitShopping(self):
		input("Press Enter to exit: ")

	def addToCartFunctionality(self, product):
		# we  need to check whether item already exists and update count to prevent overwriting items
		if(product in self.usershoppingCart):
			#add on to the current count
			self.usershoppingCart[product] = self.usershoppingCart[product] + 1
		else:
			self.usershoppingCart[product] = 1
		#probably print the users cart then prompt some more action
		self.showUsersCart()
		#print the bill finally

	def showUsersCart(self):
		#thsi will show the cart and the bill as a single unit
		print("<<<<<<<<<<<<<< SHOPPING CART >>>>>>>>>>>>>>>>>\n Item \t Count \t Total\n")
		self.cartTotal = 0;
		#check if cart is empty and show the empty cart message
		if(bool(self.usershoppingCart)):
			for key in self.usershoppingCart:
				#get the total of each item that is the price multipled by the number of items in the cart
				self.total = self.shopInventory[key] * self.usershoppingCart[key]
				self.cartTotal+=self.total
				print("{} \t {} \t {}\n".format(key, self.usershoppingCart[key], self.total))
		else:
			print("\n\n\t CART IS EMPTY")

		print("CART TOTAL - {}".format(self.cartTotal))
		self.continueShoppingorExit = input("Press 1 to Continue shopping ; 2 to proceed to checkout and 3 to exit: ")
		if(int(self.continueShoppingorExit) == 1):
			self.actionHandler()
		elif(int(self.continueShoppingorExit) == 2):
			self.checkoutCart()
		else:
			self.quitShopping()

	def checkoutCart(self):
		print("cHECKOUT THE CART BELOW\n\n\n")
		print("<<<<<<<<<<<<<< SHOPPING CART >>>>>>>>>>>>>>>>>\n Item \t Count \t Total\n")
		self.cartTotal = 0;
		#check if cart is empty and show the empty cart message
		if(bool(self.usershoppingCart)):
			for key in self.usershoppingCart:
				#get the total of each item that is the price multipled by the number of items in the cart
				self.total = self.shopInventory[key] * self.usershoppingCart[key]
				self.cartTotal+=self.total
				print("{} \t {} \t {}\n".format(key, self.usershoppingCart[key], self.total))
		else:
			print("\n\n\t CART IS EMPTY")

		print("CART TOTAL - {}".format(self.cartTotal))
		self.confirmPayment = input("\n\n\nAre you sure you want to checkout this cart? To proceed presss 1, to cancel press 2: ")
		if(int(self.confirmPayment) == 1):
			#at this point invoke the other package we'd created in level 1 to now return our change
			newChange = CashierChange()
			input("Thankyou for shopping with us. Your order has been receieved.")
		else:
			self.actionHandler()
			#this is probably the most neutral place to redirect a user to without clearing their cart
		
			

cart = Shop()
# newChange = CashierChange()