 # What is loops --> Code that repeats.

 # While loopa = a block code that repeats otself untill triggerinG
 # conditioning is no longer TRUE. CAN BE INFINITE

 # for loops = a type of loop (code block that repeats itself) BUT
 # its only repeats itself upto a certain number of times.
 # IT IS FINITE

 # THINK OF FOR LOOPS AS THE COUNTING LOOP = FOR --> 4 = number of loop

 # FOR LOOP SYNTAX
 # i stand for interator = programmers decided make this the universal
 # symbol for a placeholder for counting

 for i in range(1, 5):
     print(i)

 for i in "school":
     print(i)

 # List --> A collection type that acts as a container for
 # multiple data types and peices of data.
  
 # List syntax
 # A list is written like a variable BUT after the equal assighnment
 # symbol we are SQUARE BRACKETS and put all datas inside of
 # them. 

 fooditem1= "popcorn" #we can only store 1 piece of data in 1 variable

 groceryList = ["popcorn", "apples", "water","chips", "fish", "celery"]
 print(groceryList)

 for groceryItem in groceryList:
     print("I need to buy " + str (groceryItems))

 iremPrices = [10.00, 20.00, 13.25, 7.95, 349.00]   
 tax = 0.07

 for i in itemprice:
     # I want to know how much in taxes i need to pay on each item
     print(tax * cost)

 semesterGrades = [90, 100, 78, 74, 82, 84, ]

 for i in semesterGrades:
     # I want to find ALL the grades lower than 85.
     if i < 85:
         print(i)  


 # List are collection types for storing multiple peices of data
 # Key elements and purposes for list:
 # list are organized and structured
 # List can be manipulated and modified - mutable (mean changeable)
 # List items are accesessiable and usale

 # whem we wamt acess and item is in a list we use the indexing system
 # every item is numbered.
 # a list index always starts at zero (0)

 inventory= ["sword", " sheild", "healing potion", "armour"]

 print(inventory[0]) # indicated im going to first position in the list

# When we want add an item to our list, we use the append() method

# Use a method to remove the "healing" potion from the list

# Use a "warhammer" to the end of the list

# Use a method to add a new "healing potion" to index 4 of the list



inventory = ["sword", "shield", "healing potion", "armour"]

# Print the first item in the list
print(inventory[0])

# Remove the healing potion from the list
inventory.remove("healing potion")

# Add a warhammer to the end of the list
inventory.append("warhammer")

# Add a new healing potion at index 4
inventory.insert(4, "healing potion")

# Print the updated inventory
print(inventory)




