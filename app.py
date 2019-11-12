#program to help a cashier give change!!
#it should work on the terminal
#TODO PROGRAM HAS TWO INPUTS
#INPUT 1. amount due as change entered by the cashier
#INPUT 2. amount to be issued by the customer in terms of notes and coins
#This snipped assumes the user does not pass duplicate denominations****
#NOTE THAT THE CODE BELOW ASSUMES THAT THE USER DOES NOT ENTER DUPLICATE DENOMINATION VALUES AND THERE ARE NO COMMAS BEFORE THE DENOMINATIONS ENTERED 

class CashierChange():
	"""docstring for CashierChange"""
	def __init__(self):
		super(CashierChange, self).__init__()
		#request value here
		self.placeholder = input("CASHIER: Enter your value here: ")
		self.setChangeValue(self.placeholder)

	def setChangeValue(self, change):
		self.customerChange = int(change)
		# print(self.customerChange)
		self.getDenominations();

	def getDenominations(self):
		# this will accept denominations that the user would prefer to get their change in
		# or enter comma seperated denominations?
		self.denominations = input("CUSTOMER: Enter our preferred comma seperated denominations: eg 2, 5, 1 here: ").rstrip(',')
		self.denomListString = self.denominations.split(',');
		self.denomListInts = [int(i) for i in self.denomListString]
		self.retAmountToReturn(self.denomListInts)
		# print(self.denomListInts)

	def retAmountToReturn(self, clientDenominations):
		clientDenominations.sort(reverse=True);
		#reversed the denominations list to begin seperating the change starting off with the largest denominations
		# print(clientDenominations);
		# print(len(clientDenominations));
		print("denomination \t (count)");
		for self.x in clientDenominations:
			# print(self.x)
			#print out the denominations and the count
			if(clientDenominations.index(self.x) == 0):
				#if the first value has no remainder on the total change then break
				if(self.customerChange % self.x) == 0:
					self.count = self.customerChange//self.x
					print("{} \t ({})".format(self.x, self.count))
					#the above line should only print once if this is item 0 in the list
					break
				else:
					self.count = self.customerChange//self.x
					#update the total minus this denomination is subtracted
					self.customerChange = self.customerChange - self.x * self.count
					print("{} \t ({})".format(self.x, self.count))
			else:
				#in this case we will work with the change minus the denomination* count for position 1
				# ensure that the balance is not zero
				# print(self.customerChange)
				if(self.customerChange != 0):
					if(self.customerChange % self.x) == 0:
						self.count = self.customerChange//self.x
						print("{} \t ({})".format(self.x, self.count))
						#the above line should only print once if this is item 0 in the list
						break
					else:
						self.count = self.customerChange//self.x
						#update the total minus this denomination is subtracted
						self.customerChange = self.customerChange - self.x * self.count
						print("{} \t ({})".format(self.x, self.count))
				

	
		
# newChange = CashierChange() #commenting this out for level 2 solution
#step 1 request change to return from cashier
#delay exit from terminal
# input("Press Enter to exit program? ") # commenting this out for level 2 solution
