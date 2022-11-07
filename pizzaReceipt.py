import math
# import the math

# generate reciept for a given order of pizzas (refer to order.py)
def generateReceipt(pizzaOrder):
    
    # checks if the there are pizza orders
    if len(pizzaOrder) < 1:
        
        # prompts the user that nothing was orders and terminates the function with "return"
        print("You did not order anything")
        return
        
    # save how many pizzas have been ordered
    ORDERLENGTH = len(pizzaOrder)
    
    # declare the receipt string
    receipt = "Your order: \n"
    
    # declare the total cost (this is where all the costs will add into)
    total = 0
    
    # iterates for the number of orders 
    for i in range(ORDERLENGTH):
        
        # finds the pizza size of the current order
        pizzaSize = pizzaOrder[i][0]  
        
        # finds the list of toppings in the order
        pizzaToppings = pizzaOrder[i][1]
        
        # stores how many toppings are in the current order
        numOfToppings = len(pizzaToppings)
           
        # checks if the pizza is a SMALL
        if pizzaSize.upper() == "S":
            
            # decalre the current cost of pizza and extra toppings
            cost = 7.99
            additionalTopping = 0.50
        
        # checks if the pizza is a MEDIUM
        elif pizzaSize.upper() == "M":
            
            # decalre the current cost of pizza and extra toppings
            cost = 9.99
            additionalTopping = 0.75
            
        # checks if the pizza is a LARGE
        elif pizzaSize.upper() == "L":
            
            # decalre the current cost of pizza and extra toppings
            cost = 11.99
            additionalTopping = 1.00
            
        # checks if the pizza is a X-LARGE
        elif pizzaSize.upper() == "XL":
            
            # decalre the current cost of pizza and extra toppings
            cost = 13.99
            additionalTopping = 1.25
        
        # if there is somehow an invalid pizza size valid then terminate the program
        else:
            return
        
        # creates a reciept line stating the pizza number, size, and cost (uses the addSpaces function to make all lines even)
        receipt += addSpaces("Pizza {}: {}".format(i + 1, pizzaSize), str(cost))
        
        # takes every topping in and individually adds it to the end of the reciept
        for topping in pizzaToppings:
            receipt += "- {} \n".format(topping)
            
        # checks if he have more than 3 toppings (these are our extra toppings)
        if numOfToppings > 3:
            
            # add a line on the receipt for every extra topping. And the cost of the extra toppings (depends on the size)
            receipt += addSpaces("Extra Topping ({})".format(pizzaSize), "%.2f" % additionalTopping) * (numOfToppings - 3)
            
            # adds the total of the extra toppings to our overall total of the receipt
            total += additionalTopping * (numOfToppings - 3)
        
        # adds the cost of the current pizza to the total
        total += cost
    
    # finds tax (for 13%) and rounds to the nearst 2 decimals
    TAX = round(total * 0.13, 2)
    
    # adds the tax to the total
    total = round(total + TAX, 2)
    
    # adds line for the cost of tax on the receipt
    receipt += addSpaces("Tax:", "%.2f" % TAX)
    
    # adds a line for the total cost and removes the last enter
    receipt += addSpaces("Total:", "%.2f" % total).replace("\n", "")
    
    print(receipt)
    # return receipt


# function takes in two parameters and returns a concatenated string with spaces inbetween
def addSpaces(strStart, strEnd):
    # declare the total number of character we want the end string
    numOfSpace = 32
    
    # delare the string that holds our spaces
    spaces = ""
    
    # finds how many characters the first and second parameter combined out
    totalString = len(strStart + strEnd)
    
    # checks if the total number of characters is less than number of characters we want
    if totalString < numOfSpace:
        
        # stores the number of spaces need to make the string even
        spaces = " " * (numOfSpace - totalString)
    
    # returns the two strings with the space inbetween and a new line
    return strStart + spaces + strEnd + "\n"