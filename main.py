# D300 Samantha Chung
# Sept 28 2020
# Robust ChatBot

# Customer is at a bubble tea cafe and the robot is taking the customers orders. 
# 1. The robot would ask if they would like to order. Giving a menu. (String methods and nested if/else)
# 2. If yes, chatbot will ask for specifications like: size, toppings and how many cups they'd like. (Loop and in keyword)
# 3. Loop for different toppings they would like.
# 4. if no or else, end convo

import random

print ("Hello! Welcome to BoboTea")
print ("We are selling 3 types of drinks. Milk tea, Mango Slush and Matcha Latte")
print ("Would you like to buy a drink?")
order = input()
# First question asks if they want to order something
# Statement uses 2 string methods
if order.lower().strip(".!") == 'yes':
  print ("Great! We are selling 3 cup combos. Would you like 3 drinks?")
  amount = input().lower().strip('.!,?')
  # One of many nested conditionals. (if/else statements)
  if amount == 'yes':
    # Second asks if toppings are wanted
    print ("Great, would you like any toppings?")
    topping = input().lower().strip('.!,?')
    if topping == 'yes':
      # This loop will go through each drink on the menu and ask what topping they would like. When have gon through each, the loop ends.
      # This statement uses the in keyword and the for loop
      for drink in ["Milk tea", "Mango Slush", "Matcha Latte"]:
        print ("What topping would you like in your",drink)
        input()
      print ("Ok! Your total for today comes to $18.")

      # A new list is created to generate an oorder number to complete the transaction.
      number = ['1','2','3','4','5','6','7','8','9','10']
      order_number = random.choice(number)
      print ("Here is your order number:", order_number)
      print ("Thank you for coming!")

    elif topping == "no":
      #Asks topping again in second branch
      print ("Was there another topping you wanted?")
      other_topping = input().lower().strip(".!")
      if other_topping == 'yes':
        print ("Ok what would you like?")
        # Asks for desired topping and uses the input in to next line
        other_topping_a = input()
        print ("Lucky you! We", other_topping_a, "in stock. Your total now comes to $17.")
        number = ['1','2','3','4','5','6','7','8','9','10']
        order_number = random.choice(number)
        print ("Here is your order number:", order_number)
        print ("Thank you for coming!")
      elif other_topping == 'no':
        print ("No problem, your total comes to $15")
        number = ['1','2','3','4','5','6','7','8','9','10']
        order_number = random.choice(number)
        print ("Here is your order number:", order_number)
        print ("Thank you for buying!")
      else:
        print ("Your order is incomplete and cancelled.")

# Going forward code will be reused to create flow
    else:
      print ("I do not understand. Was there another topping you wanted?")
      extra_topping = input().lower().strip(".!")
      if extra_topping == 'yes':
        print ("Ok what would you like?")
        extra_topping_a = input()
        print ("Lucky you! We", extra_topping_a, "in stock. Your total now comes to $17.")
        number = ['1','2','3','4','5','6','7','8','9','10']
        order_number = random.choice(number)
        print ("Here is your order number:", order_number)
        print ("Thank you for coming!")
      elif extra_topping == 'no':
        print ("No problem, your total comes to $15")
        number = ['1','2','3','4','5','6','7','8','9','10']
        order_number = random.choice(number)
        print ("Here is your order number:", order_number)
        print ("Thank you for buying!")
      else:
        print ("Your order is incomplete and cancelled.")
  elif amount == 'no':
    print ("Oh ok. Would you like 1 drink?")
    single_drink = input().lower().strip(".!")
    if single_drink == 'yes':
      print ("Great! Which one would you like?")
      print ("We are selling 3 types of drinks. Milk tea, Mango Slush and Matcha Latte") 
      drink_type = input()
      print ("Would you like any toppings?")
      topping2 = input().lower().strip(".!")
      if topping2 == 'yes':
        print ("Ok, what topping would you like?")
        input()
        print ("Ok your total comes to $6.")
        number = ['1','2','3','4','5','6','7','8','9','10']
        order_number = random.choice(number)
        print ("Here is your order number:", order_number)
        print ("Thank you for coming!")
      elif topping2 == 'no':
        print ("Ok your total comes to $5.50.")
        number = ['1','2','3','4','5','6','7','8','9','10']
        order_number = random.choice(number)
        print ("Here is your order number:", order_number)
        print ("Thank you for coming!")
      else:
        print ("I'm not sure what you mean. Your order has been cancelled.")
    elif single_drink == 'no':
      print ("I can't sell you anything then. We only sell drinks in threes or single cups.")
      print ("Goodbye.")
    else:
      print ("I'm not sure what you mean. Your order has been cancelled.")
elif order.lower().strip(".!") == "no":
  print ("No problem! Have a great day!")
else:
  print ("I'm not sure what you mean. Goodbye.")
 