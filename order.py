# import the generate reciept function
import pizzaReceipt

# declare valid toppings choices
TOPPINGS = ('ONION', 'SPINACH', 'HAM', 'TOMATO', 'BROCCOLI', 'BACON', 
            'GREEN PEPPER', 'PINEAPPLE', 'GROUND BEEF', 'MUSHROOM', 
            'HOT PEPPER', 'CHICKEN', 'OLIVE', 'PEPPERONI', 'SAUSAGE')

# prompts the user to order a pizza
def order():
    # stop conditions for the program to stop (checks if the user input is within this string)
    terminate = ["q", "no"]
    
    # valid sizes for pizzas
    validSize = ['s', 'm', 'l', 'xl']
    
    # stores all of user's pizza orders
    totalOrder = []
        # (ie. [["S", [olive, mushroom]],["XL", [olive, ground beef]]])
    
    # stores one of the user's pizza order at a time
    order = []
        # ie (["S", [olvice, mushroom]])
    
    # stores one of the user's pizza's toppings
    toppingList = []
        # (ie. [pepperoni, mushroom])
    
    
    # askes user if they want to order a pizza
    path = input("Do you want to order a pizza? ")
    
    # checks if users input is not in terminate (if user input is in termiate then stop while loop)
    while path.lower() not in terminate:
        
        # asks user to select a given size
        prompt = "Choose a size: S, M, L, or XL: "
        pizzaSize = input(prompt)
        
        # if user input is not a valid input (meaning no inside validSize)
        # keep looping and asking the user to enter a size
        while pizzaSize.lower() not in validSize:
            pizzaSize = input(prompt)
            
        # adds size to current order of the pizza
        order.append(pizzaSize)
        
        
        # prompts the user to enter a topping to add on the pizza
        prompt = 'Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". When you are done adding toppings, enter "X"\n'
        userToppings = input(prompt)
        
        # while user the wants to keep adding toppings ()
        while userToppings.lower() != "x":
            
            # if the user types "list", the list of toppings will be printed for the user
            if userToppings.lower() == "list":
                # print("\n" + str(TOPPINGS)) 
                print(str(TOPPINGS)) 
                
            # checks if the topping is a valid topping 
            # if yes, then add the topping to the user's current pizza
            elif userToppings.upper() in TOPPINGS:
                toppingList.append(userToppings)
                print("Added {} to your pizza\n".format(userToppings))
            
            # prompts the user to add more toppings
            userToppings = input(prompt)
        
        # add a copy of the topping list AS A TUPLE to current order
        order.append(tuple(list(toppingList)))
        
        # add a copy of the current order to the total order as a TUPLE
        totalOrder.append(tuple(list(order)))
        
        # empty the current order and topping list
        order = []
        toppingList = []
        
        # ask the user to continue ordering
        path = input("Do you want to continute order? ")
        
    # prints the receipt for the given order to the user
    pizzaReceipt.generateReceipt(tuple(totalOrder))
    
order()