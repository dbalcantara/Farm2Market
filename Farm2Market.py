def draw_farm():
    print("|--------------------------------------------------------------------------------|")
    print("|    ________                                                				    |")
    print("|   |        |              _________                                _________   |")
    print("|   |    F   |             |         |    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~   |         |  |")
    print("|   |    A   |            |           | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |           | |")
    print("|---|    R   |-----------|-------------|--------------------------|-------------| ")
    print("|   |    M   |          |   ________    | ~ ~ ~    PUMPKIN    ~ ~ |   ________   |")
    print("|   |    -   |          |  |        |   |      ~ ~ ~ ~ ~ ~ ~ ~ ~  |  |        |  |")
    print("|   |    2   |          |  |  Barn  |   | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |  |  Barn  |  |")
    print("|   |    -   |          |  |________|   | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |  |________|  |")
    print("|---|    M   |----------|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|   |    A   |          |   ________    | ~ ~ ~ ~   MAIZE   ~ ~ ~ |   ________   |")
    print("|   |    R   |          |  |        |   | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |  |        |  |")
    print("|   |    K   |          |  |  Cow   |   | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |  |  Cow   |  |")
    print("|   |    E   |          |  |________|   | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |  |________|  |")
    print("|   |    T   |          |               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|-  __________   -------|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|                       |   ________    | ~ ~ ~    PUMPKIN    ~ ~ |   ________   |")
    print("|                       |  |        |   | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |  |        |  |")
    print("|                       |  |Chicken |   | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |  | Chicken|  |")
    print("|                       |  |________|   | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |  |________|  |")
    print("|                       |               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|-----------------------|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|-----------------------|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|                       |               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|                       |               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|                       |               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|-----------------------|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|                       |    ________   | ~ ~ ~ ~   MAIZE   ~ ~ ~ |    ________  |")
    print("|                       |   |        |  | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |   |        | |")
    print("|                       |   |Tractor |  | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |   | Tractor| |")
    print("|                       |   |________|  | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |   |________| |")
    print("|-----------------------|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|                       |               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|                       |               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|-----------------------|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|        ~ ~ ~ ~ ~ ~ ~ ~|     ~ ~ ~ ~ ~ | ~ ~ ~ ~   MAIZE   ~ ~ ~ |    ~ ~ ~ ~ ~ |")
    print("|       ~ ~ ~ ~ ~ ~ ~ ~ |     ~ ~ ~ ~ ~ | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |    ~ ~ ~ ~ ~ |")
    print("|-----------------------|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|-----------------------|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|                       |               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|                       |               | ~ ~ ~   PUMPKIN   ~ ~ ~ |              |")
    print("|-----------------------|               | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |              |")
    print("|                         ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~|")
    print("|--------------------------------------------------------------------------|")
    
# Call the function to draw the farm
draw_farm()




def introduction(products): #this function contains the introduction for the game and explains the gameplay
	print()
	print()
	print()
	name = input("Enter Player's Name: ")
	print()
	print()
	print("-------------------------------------- Welcome to Farm2Market --------------------------------------")
	print()
	print("Welcome", name, "! This is a farm simulation game. In this game, you are given the role of a farmer.")
	print("You have been given a capital amount of PHP 5,000 by the government.")
	print()
	print("Current budget:   ", products["budget"])
	print("Use this to expand your farm.")
	print()
	print()
	return

def menu(): #this function contains the main menu and asks for the user's options on what to do
	print()
	print("========== Main Menu ==========")
	print()
	print("[1] Visit my farmlot")
	print("[2] Visit item shop")
	print("[3] Plant my seeds")
	print("[4] Place livestock")
	print("[5] Harvest my farm produce")
	print("[6] Sell my farm produce")
	print("[7] Show Inventory")
	print("[8] Load Previous Game")
	print("[0] Exit game")
	print()
	print("===============================")
	print()
	choice = input("Choose an option: ")
	print()
	return choice

def farmVisit(layout): # this function will display the legend for crops and livestock, and farm layout
	print("========== Farm Layout ========")
	print()
	print("Legend:") # legend of the crops and livestock
	print(" * --> Maize")
	print(" $ --> Pumpkin")
	print(" > --> Chicken")
	print(" O --> Cow")
	print()
	for k,v in layout.items(): # a for loop that will display the farm layout in a 2D format
		print(k, v["icon"], v["time"])
	print()
	print("===============================")

def itemShop(products): # this function will display the item shop
	print("=========== Item Shop ==========")
	print()
	print("Your current budget is: ", products["budget"]) # this line of code will display the current budget
	print()
	print("[1] Buy 1 Farm Lot    @5000.00")
	print("[2] Buy Maize           @80.00")
	print("[3] Buy Pumpkin Seeds   @12.00")
	print("[4] Buy Chicken       @1000.00")
	print("[5] Buy Cow          @20000.00")
	print("[0] Go back to main menu")
	print()
	print("===============================")
	print() 
	choice = input("What would you like to buy? ")
	return choice
	
def farmPlant(products): # this function will be used when the user decided to plant seeds
	print("======== Crop Inventory =======")
	print()
	print("Maize: ", products["maize"]) # this line of code will display the number of maize available 
	print("Pumpkin: ", products["pumpkin_seeds"]) # this line of code will display the number of pumpkin seeds available 
	print()
	print("===============================")
	print()
	print("[1] Maize")
	print("[2] Pumpkin")
	choice = input("What would you like to plant? ") # this line of code will ask the user what seed to plant 
	print()
	return choice

def farmLivestock(products): # this function will be used when the user decided to place livestock
	print("===== Livestock Inventory =====")
	print()
	print("Chicken: ", products["chicken"]) # this line of code will display the number of chicken available 
	print("Cow: ", products["cow"]) # this line of code will display the number of cow available 
	print()
	print("===============================")
	print()
	print("[1] Chicken")
	print("[2] Cow")
	choice = input("What would you like to place? ") # this line of code will ask the user what livestock to place 
	print()
	return choice

def farmInventory(inventory): # this function will display the inventory
	print("======== Farm Products ========")
	print()
	for k, v in inventory.items(): # a for-loop that will display the the dictionary in 2D format
		print (k, ":", v)
	print()
	print("===============================")
	print()
	return inventory

def saveLayout(layout): # this line of code will save the farm layout when the game is saved
	farm_layout = open("farmlot.txt","w") # this line of code will open the farmlot.txt
	for k,v in layout.items():
		farm_layout.write(str(k)+"\n") # this line of code will write the farm lot number from the layout dictionary to farmlot.txt
		farm_layout.write(str(v["icon"])+"\n") # this line of code will write the icon from the layout dictionary to farmlot.txt
		farm_layout.write(str(v["time"])+"\n") # this line of code will write the time from the layout dictionary to farmlot.txt
	farm_layout.close() # this line of code will close the farmlot.txt
	
def loadLayout(layout): # this line of code will load and update the farm layout from the previous saved game
	farm_layout = open("farmlot.txt","r") # this line of code will open the farmlot.txt
	x = [] # a list to locate the codes written in the farmlot.txt 
	for line in farm_layout: # a for loop to append the each line of code from the farmlot.txt to the x-list
		x.append(line[:len(line)-1])
	
	for i in range(0,len(x),3): # for loop that will update the current farm layout to the farm layout from the previous game
		new_lot = {} # a dictionary to locate the previous game's farm layout from farmlot.txt 
		layout[int(x[i])] = new_lot # this line of code will change the current farm layout to the previous game's farm layout
		new_lot.update({"icon":str(x[i+1])}) # this line of code will change the current icon to the previous game's icon 
		if x[i+2] != "_":
			new_lot.update({"time":datetime.strptime(x[i+2], '%Y-%m-%d %H:%M:%S.%f')}) # this line of code will change the current time to the previous game's time 
		else:
			new_lot.update({"time":x[i+2]})
	farm_layout.close() # this line of code will close the farmlot.txt
	return layout

def saveProducts(products): # this line of code will save the products when the game is saved
	farm_products = open("products.txt","w") # this line of code will open the products.txt
	for k,v in products.items(): # a for loop that will write each keys and values in the products to products.txt
		farm_products.write(str(k)+":"+str(v)+"\n")
	farm_products.close() # this line of code will open the products.txt


def loadProducts(products): # this line of code will load and update the products from the previous saved game
	farm_products = open("products.txt","r") # this line of code will open the products.txt
	for line in farm_products: # a for loop that will update each keys and values in the inventory to inventory.txt
		k, v = line.split(":")
		products.update({str(k):int(v)})
	farm_products.close() # this line of code will close the products.txt
	return products

# this lines of code below is a dictionary of all the products and their corresponding number of items
products = {"budget":5000, 
			"lot":1, 
			"block": 10, 
			"cow": 0,
			"chicken": 0, 
			"egg": 0, 
			"maize": 0, 
			"corn": 0, 
			"pumpkin_seeds":0 , 
			"pumpkin": 0}

layout = {} # an empty dictionary where the farm layout will be located	

from datetime import timedelta, datetime # this line of code will import the date and time

introduction(products) # this line of code will call the function for introduction
while True:
	choice = menu() # this line of code will call the function for menu
	i = 1
	while i <= products["block"]: # a while loop will update the empty dictionary with keys and values
		if i in layout.keys(): # will iterate the loop until it reaches the number of blocks 
			i = i + 1
		else:
			layout[i] = {"icon":"_", "time":"_"} # this line of code will update the empty dictionary with keys and values 

	if choice == "1": # if user wants to visit farm layout
		farmVisit(layout) # this line of code will call the function for farm layout
	
	elif choice == "2": # if user wants to buy items
		while True:
			choice = itemShop(products) # this line of code will call the function for item shop
			if choice == "0": # if user wants to go back to main menu
				break

			elif choice == "1": # if user wants to buy a farm lot
				lot_num = int(input("How many farm lot would you like to buy? ")) # ask the user for the quantity of desireed farmlot
				print()
				if products["budget"] >= 5000 * products["lot"]: # if the budget is greater than or equal to the amount of farmlot multiplied to the desired quantity
					products["budget"] = products["budget"] - (5000 * lot_num) # will subtract the total cost from the budget
					products["lot"] = products["lot"] + lot_num # will add the number of bought lot/s to products
					products["block"] = products["block"] + (10 * lot_num) # will add 10 blocks per 1 lot bought
					print("You have successfully bought", lot_num, "farm lot/s.") 
					print()
					break
				
				else:
					print("You don't have enough money yet.")
					print()


			elif choice == "2": # if user wants to buy a maize
				maize_num = int(input("How many maize would you like to buy? ")) # ask the user for the quantity of desired maize
				print()
				if products["budget"] >= 80 * maize_num: # if the budget is greater than or equal to the amount of maize multiplied to the desired quantity
					products["budget"] = products["budget"] - (80 * maize_num) # will subtract the total cost from the budget
					products["maize"] = products["maize"] + (6 * maize_num) # will add the number of bought maize/s to products
					print("You have successfully bought", maize_num, "maize.")
					print()
					break

					
				else:
					print("You don't have enough money yet.")
					print()


			elif choice == "3": # if user wants to buy a pumpkin seeds
				pumpkin_num = int(input("How many pumpkin seed/s would you like to buy? ")) # ask the user for the quantity of desired pumpkin seeds
				print()
				if products["budget"] >= 12 * pumpkin_num: # if the budget is greater than or equal to the amount of pumpkin seeds multiplied to the desired quantity
					products["budget"] = products["budget"] - (12 * pumpkin_num) # will subtract the total cost from the budget
					products["pumpkin_seeds"] = products["pumpkin_seeds"] + pumpkin_num # will add the number of bought pumpkin seed/s to products
					print("You have successfully bought", pumpkin_num, "pumpkin seed/s")
					print()
					break

				else:
					print("You don't have enough money yet.")
					print()

			elif choice == "4": # if user wants to buy a chicken
				chicken_num = int(input("How many chicken/s would you like to buy? ")) # ask the user for the quantity of desired chicken
				print()
				if products["budget"] >= 1000 * chicken_num: # if the budget is greater than or equal to the amount of chicken multiplied to the desired quantity
					products["budget"] = products["budget"] - (1000 * chicken_num) # will subtract the total cost from the budget
					products["chicken"] = products["chicken"] + chicken_num # will add the number of bought chicken/s to products
					print("You have successfully bought", chicken_num, "chicken/s")
					print()
					break

				else:
					print("You don't have enough money yet.")
					print()

			elif choice == "5": # if user wants to buy a cow
				cow_num = int(input("How many cow would you like to buy? ")) # ask the user for the quantity of desired cow
				print()
				if products["budget"] >= 20000 * cow_num: # if the budget is greater than or equal to the amount of cow multiplied to the desired quantity
					products["budget"] = products["budget"] - 1000 * cow_num # will subtract the total cost from the budget
					products["cow"] = products["cow"] + cow_num # will add the number of bought cow/s to products
					print("You have successfully bought", cow_num, "cow/s")
					print()
					break

				else:
					print("You don't have enough money yet.")
					print()

	elif choice == "3": # if user wants to plant seeds
		choice = farmPlant(products) # this line of code will call the function for planting seeds
		if choice == "1": # if user wants to plant maize
			if products["maize"] == 0: 
				print("No maize found in the inventory.")
			else:
				while True:
					print("[1] Yes")
					print("[0] Go Back to Main Menu")
					choice = input("Would you like to plant a maize? ")
					print()
					if choice == "1":
						print("Maize requires 1 farm bed.")
						lot = int(input("Choose a Farm Lot (1-10): ")) # will ask user for the farmlot to plant on
						print()
						if lot in layout.keys():
							if layout[lot]["icon"] == "_": # if farmlot is empty		
								layout[lot].update({"icon":"*"}) # will update icon to the layout
								products["maize"] = products["maize"] - 1 # will subtact the planted maize from the total number of maize
								layout[lot].update({"time":datetime.now() + timedelta(minutes=1)}) # will set the remaining time before harvest
								print("You have successfully planted a maize on your farmlot.")
								print()
								break
							else:
								print("Farm lot is already occupied.") 
								print()
						else:
							print("Invalid Input.")
							print()

					elif choice == "0":
						break

					else:
						print("Invalid Input.")
						print()
						break

		if choice == "2": # if user wants to plant pumpkin seeds
			if products["pumpkin_seeds"] == 0:
				print("No pumpkin seeds found in the inventory.")
				print()
			else:
				while True:
					print("[1] Yes")
					print("[0] Go Back to Main Menu")
					choice = input("Would you like to plant a pumpkin seed? ") 
					print()
				
					if choice == "1":
						print("Pumpkin seeds require 2 farm beds.")
						lot = int(input("Choose 2 (consecutive) Farm Lot(1-10) : ")) # will ask user for the farmlot to plant on
						lot_1 = int(input("Choose another Farm Lot (1-10): "))
						print()
						if lot + 1 == lot_1: # if user's farm lot input is consecutive
							if layout[lot]["icon"] and layout[lot_1]["icon"] == "_": # if farmlot is empty				
								layout[lot].update({"icon":"$"}) # will update the icon to the layout
								layout[lot_1].update({"icon":"$"}) # will update the icon to the layout
								products["pumpkin_seeds"] = products["pumpkin_seeds"] - 1 # will subtract the planted seed total number pumpkin seeds
								layout[lot].update({"time":datetime.now() + timedelta(minutes=1)}) # will set the remaining time before harvest
								layout[lot_1].update({"time":datetime.now() + timedelta(minutes=1)}) # will set the remaining time before harvest
								print("You have successfully planted a pumpkin seed on your farm lot.")
								print()
								break

							else:
								print("Farm lot is already occupied.")
								print()
						else:
							print("Farm lot/s are not consecutive farm lots. Choose another one")
							print()
						

					elif choice == "0":
						break

					else:
						print("Invalid Input.")
						print()

	elif choice == "4": # if user wants to place livestock
		choice = farmLivestock(products) # this line of code will call the function for placing livestock
		if choice == "1": # if user wants to plant maize
			if products["chicken"] == 0: 
				print("No chicken found in the inventory.")
			else:
				while True:
					print("[1] Yes")
					print("[0] Go Back to Main Menu")
					choice = input("Would you like to place a chicken? ")
					print()
					if choice == "1":
						print("Chicken requires 1 coop.")
						lot = int(input("Choose a Farm Lot (1-10): ")) # will ask user for the farmlot to plant on
						print()
						if lot in layout.keys():
							if layout[lot]["icon"] == "_": # if farmlot is empty		
								layout[lot].update({"icon":">"}) # will update icon to the layout
								products["chicken"] = products["chicken"] - 1 # will subtact the planted maize from the total number of maize
								layout[lot].update({"time":datetime.now() + timedelta(minutes=1)}) # will set the remaining time before harvest
								print("You have successfully placed a chicken in your coop.")
								print()
								break
							else:
								print("Farm lot is already occupied.") 
								print()
						else:
							print("Invalid Input.")
							print()

					elif choice == "0":
						break

					else:
						print("Invalid Input.")
						print()
		
		if choice == "2": # if user wants to plant maize
			if products["cow"] == 0: 
				print("No cow found in the inventory.")
			else:
				while True:
					print("[1] Yes")
					print("[0] Go Back to Main Menu")
					choice = input("Would you like to place a cow? ")
					print()
					if choice == "1":
						print("Cow requires 1 cowshed.")
						lot = int(input("Choose a Farm Lot (1-10): ")) # will ask user for the farmlot to plant on
						print()
						if lot in layout.keys():
							if layout[lot]["icon"] == "_": # if farmlot is empty		
								layout[lot].update({"icon":"O"}) # will update icon to the layout
								products["cow"] = products["cow"] - 1 # will subtact the planted maize from the total number of maize
								layout[lot].update({"time":datetime.now() + timedelta(minutes=1)}) # will set the remaining time before harvest
								print("You have successfully placed a cow in your cowshed.")
								print()
								break	
							else:
								print("Farm lot is already occupied.")
								print() 
						else:
							print("Invalid Input.")
							print()

					elif choice == "0":
						break

					else:
						print("Invalid Input.")

	elif choice == "5": # if user wants to harvest products
		lot = int(input("Harvest Farm Lot (1-10):  ")) # will ask user for the farmlot to harvest from
		lot_1 = lot + 1
		print()
		while True:
			if layout[lot]["icon"] == "_": # if farmlot is empty
				print("Farm lot is empty.")
				break

			elif layout[lot]["icon"] == "*": # if maize is planted
				if layout[lot]["time"] <= datetime.now(): # if the no remaining time left before harvest
					layout[lot].update({"icon":"_"}) # will empty the farmlot
					products["corn"] = products["corn"] + 30 # will add 30 corns to the total number of corns
					layout[lot].update({"time":"_"}) # will empty the farmlot
					print("30 corns are added to your inventory.")
					print()
					break
				else:
					print("This farm lot is not available for harvest.")
					print()
					break

			elif layout[lot]["icon"] == "$": # if pumpkin is planted
				if layout[lot]["time"] <= datetime.now(): # if the no remaining time left before harvest
					layout[lot].update({"icon":"_"}) # will empty the farmlot
					layout[lot_1].update({"icon":"_"}) # will empty the farmlot
					products["pumpkin"] = products["pumpkin"] + 4 # will add 4 pumpkin to the total number of corns
					layout[lot].update({"time":"_"}) # will add 30 corns to the total number of corns
					layout[lot_1].update({"time":"_"}) # will add 30 corns to the total number of corns
					print("4 pumpkins are added to your inventory.")
					print()
					break
				else:
					print("This farm lot is not available for harvest.")
					print()
					break

			elif layout[lot]["icon"] == ">": # if chicken is placed
				if layout[lot]["time"] <= datetime.now(): # if the no remaining time left before harvest
					products["eggs"] = products["egg"] + 6 # will add 6 pumpkin to the total number of corns
					print("6 eggs are added to your inventory.")
					print()
					break
				else:
					print("This farm lot is not available for harvest.")
					print()
					break

			else:
				print("Farm lot does not exist.")
				print()
				break
	

	elif choice == "6": # if user wants to sell products
		# this lines of code below is a dictionary of the inventory and their corresponding number of items
		inventory = {"Budget": products["budget"],
			"[1] Maize": products["maize"], 
			"[2] Corn": products["corn"], 
			"[3] Pumpkin Seeds": products["pumpkin_seeds"], 
			"[4] Pumpkin": products["pumpkin"], 
			"[5] Chicken": products["chicken"], 
			"[6] Eggs": products["egg"], 
			"[7] Cow": products["cow"]}

		print("======== Farm Products ========")
		print()
		for k, v in inventory.items(): # a for-loop that will display the the dictionary in 2D format
			print (k, ":", v)
		print()
		print("===============================")
		print()
		print("[0] Go Back to Main Menu")
		print()
		while True:
			choice = input("What would you like to sell? ") # will ask the user what to sell
			print()
			if choice == "1": # if user wants to sell maize
				if products["maize"] == 0:
					print("You don't have any maize in your inventory.")
					print()
				elif products["maize"] >= 6: # if maize is more than or equal to 6
					num = int(input("How many maize would you like to sell? ")) # will ask the user for the number of corn to sell
					print()
					if num % 6 == 0: # if maize to sell is divisible by 6
						products["maize"] = products["maize"] - num # will subtract the sold number of maize from the total number of maize
						products["budget"] = products["budget"] + 64 # will add 64 to the budget
						print("You have sold", num,"maize for ₱64.00")
						print()	
					else: 
						print("Maize to sell should be by 6 pieces.")
						print()
				else:
					print("Not enough maize. You should have at least 6 maize.")
					print()

			elif choice == "2": # if user wants to sell corn
				if products["corn"] == 0:
					print("You don't have any corn in your inventory.")
					print()
				elif products["corn"] >= 60: # if corn is more than or equal to 60
					num = int(input("How many corn would you like to sell? ")) # will ask the user for the number of corn to sell
					print()
					if num % 60 == 0: # if corn to sell is divisible by 60
						products["corn"] = products["corn"] - num # will subtract the sold number of corn from the total number of corn
						products["budget"] = products["budget"] + 400 # will add 400 to the budget
						print("You have sold", num,"corn for ₱400.00")
						print()	
					else: 
						print("Corn to sell should be by 60 pieces.")
						print()
				else:
					print("Not enough corn. You should have at least 60 corn.")
					print()

			elif choice == "3": # if user wants to sell pumpkin seeds
				if products["pumpkin_seeds"] == 0:
					print("You don't have any pumpkin seeds in your inventory.")
					print()
				else:
					num = int(input("How many pumpkin seeds would you like to sell? ")) # will ask the user for the number of pumpkin seeds to sell
					print()
					products["pumpkin_seeds"] = products["pumpkin_seeds"] - num  # will subtract the sold number of pumpkin seeds from the total number of pumpkin seeds
					products["budget"] = products["budget"] + 9.6 # will add 9.6 to the budget
					print("You have sold", num,"pumpkin seed/s for ₱9.60")	
					print()

			elif choice == "4": # if user wants to sell pumpkin 
				if products["pumpkin"] == 0: 
					print("You don't have any pumpkin in your inventory.")
					print()
				else:
					num = int(input("How many pumpkin would you like to sell? ")) # will ask the user for the number of pumpkin to sell
					print()
					products["pumpkin"] = products["pumpkin"] - num # will subtract the sold number of pumpkin from the total number of pumpkin 
					products["budget"] = products["budget"] + 200 # will add 200 to the budget
					print("You have sold", num,"pumpkin/s for ₱200.00")
					print()

			elif choice == "5":
				if products["chicken"] == 0:
					print("You don't have any chicken in your inventory.")
					print()
				else:
					num = int(input("How many chicken would you like to sell? ")) # will ask the user for the number of chicken to sell
					print()
					products["chicken"] = products["chicken"] - num  # will subtract the sold number of chicken from the total number of chicken 
					products["budget"] = products["budget"] + 800  # will add 800 to the budget
					print("You have sold", num,"chicken seeds for ₱800.00")
					print()

			elif choice == "6":
				if products["budget"] == 0:
					print("You don't have any egg in your inventory.")
					print()
				elif products["egg"] >= 12:
					num = int(input("How many egg would you like to sell? ")) # will ask the user for the number of egg to sell
					print()
					if num % 12 == 0:
						products["egg"] = products["egg"] - num # will subtract the sold number of egg from the total number of egg 
						products["budget"] = products["budget"] + 100 # will add 100 to the budget
						print("You have sold", num,"egg for ₱100.00")	
						print()
					else: 
						print("egg to sell should be by dozen or 12 pieces.")
						print()
				else:
					print("Not enough egg. You should have at least 12 egg.")
					print()

			elif choice == "7":
				if products["cow"] == 0:
					print("You don't have any cow in your inventory.")
					print()
				else:
					num = int(input("How many cow would you like to sell? "))  # will ask the user for the number of cow to sell
					print()
					products["cow"] = products["cow"] - num  # will subtract the sold number of egg from the total number of egg 
					products["budget"] = products["budget"] + 18000  # will add 18000 to the budget
					print("You have sold", num,"cow for ₱18000.00")
					print()

			elif choice == "0":
				break

			else:
				print("Invalid Input.")
				print()

	elif choice == "7": # if user wants to display inventory
		# this lines of code below is a dictionary of the inventory and their corresponding number of items
		inventory = {"Budget": products["budget"],
			"Maize": products["maize"], 
			"Corn": products["corn"], 
			"Pumpkin Seeds": products["pumpkin_seeds"], 
			"Pumpkin": products["pumpkin"], 
			"Chicken": products["chicken"], 
			"Eggs": products["egg"], 
			"Cow": products["cow"]}

		print("======== Farm Products ========")
		print()
		for k, v in inventory.items(): # a for-loop that will display the the dictionary in 2D format
			print (k, ":", v)
		print()
		print("===============================")
		print()	

	elif choice == "8": # if the user wants to load previous game
		loadLayout(layout) # will call the function to load farm layout
		loadProducts(products) # will call the function to load products
		print("Previous game successfully loaded.")
		print()
		
	elif choice == "0": # if user wants to exit the game
		print("[1] Yes")
		print("[0] No")	
		choice = input("Are you sure you want to quit the game? ") # will ask if the user wants to quit the game
		print()
		if choice == "1": # if user wants to exit the game
			print("[1] Yes")
			print("[0] No")	
			choice = input("Would you like to save your game? ") # will ask if the user wants to save the game
			print()	
			if choice == "1": # if user wants to save current game
				saveLayout(layout) # will call the function to save farm layout
				saveProducts(products) # will call the function to save products
				print("Game successfully saved.")
				break
			if choice == "0": # if user doesn't want to save current game
				print("Thank you for playing.")
				break

		elif choice == "0": # if user wants to continue playing
			print("You're back to the game.")
			print()
		else:
			print("Invalid Input.")
			print()

	else: 
		print("Invalid Input.")	
		print()	
			
