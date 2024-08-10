"""This module contains all the functions that are used in the application."""

# Import resources from coffee_items.py module
from prog_resources.coffee_items import *
from prog_resources.format import *
from prog_resources.color import *

# Declare module_level variables
water_available = resources["water"]
coffee_available = resources["coffee"]
milk_available = resources["milk"]
money_made = 0


def add_revenue(amount):
  """Adds the amount earned to resources available"""
  resources["Money"] = '${:0,.2f}'.format(amount)

# A function to put the Coffe Machine OFF
def put_coffee_machine_off():
  """Puts the coffee machine off"""
  print()
  print(f"{bold(fg_red('Put Coffee Machine Off?'))}")
  input("Press Enter to continue ...\n")
  clear()
  exit()

# Function to present report on the resources available
def print_report():
  clear()
  add_revenue(money_made)
  print(f"{bold(underline(fg_violet('REPORT ON RESOURCES AVAILABLE')))}")
  for key in resources:
    if key == "coffee":
      print(f"\t{italic(fg_violet(key))} : \t{italic(fg_green(resources[key]))}g")
    elif key == "water" or key == "milk":
      print(f"\t{italic(fg_violet(key))} : \t{italic(fg_green(resources[key]))}ml")
    else:
      print(f"\t{italic(fg_violet(key))} : \t{italic(fg_red(resources[key]))}")
  print(f"{bold(fg_violet('...............................'))}")

def is_resources_sufficient(coffee_type):
  resources_alert = ""
  global water_required
  water_required = MENU[coffee_type]["ingredients"]["water"]
  global coffee_required
  coffee_required = MENU[coffee_type]["ingredients"]["coffee"]
  if coffee_type == "espresso":
    global milk_required
    milk_required = 0
  else:
    milk_required = MENU[coffee_type]["ingredients"]["milk"]
  
  if water_available > water_required and coffee_available > coffee_required and milk_available > milk_required:
    return True

# Function to calculate amount paid
def calculate_payment(quarters, dimes, nickles, penny):
  """Returns the sum of the amounts paid by the user"""
  return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (penny * 0.01)

# Function to check if payment is sufficient
def is_payment_sufficient(coffee_type, amount):
  """Returns true if the payment made is sufficient. It takes type of coffee ordered and the amount paid as inputs"""
  coffee_cost = MENU[coffee_type]["cost"]
  if amount >= coffee_cost:
    return True
  else:
    return False

# Function to return change if amount paid is greater than required
def give_change(coffee_type, amount):
  """Returns a change to be given to user""" 
  coffee_cost = MENU[coffee_type]["cost"]
  if is_payment_sufficient and amount > coffee_cost:
    change = amount - coffee_cost
    formatted_change = '${:0,.2f}'.format(change)
    message = f"Here is {formatted_change} in change."
    return message

# Function to make coffee
def make_coffee(coffee_type):
  global water_available
  global coffee_available
  global milk_available
  water_available -= water_required
  coffee_available -= coffee_required	
  milk_available -= milk_required
  resources["water"] = water_available
  resources["coffee"] = coffee_available
  resources["milk"] = milk_available
  global money_made
  money_made += MENU[coffee_type]["cost"]

# Function to return the cost of coffee ordered by user
"""This function returns the cost of the coffee ordered by the customer"""
def get_coffee_cost(coffee_type):
  cost = MENU[coffee_type]["cost"]
  formatted_cost = '${:0,.2f}'.format(cost)
  return formatted_cost

# Function to return the amount paid by the user
def format_amount(amount):
  formatted_amount = '${:0,.2f}'.format(amount)
  return formatted_amount

# Function to display sorry message.
def display_sorry_message(message):
  """Formats a sorry message. It formats the text to display in red to alert the user that there is something wrong with the machine or to indicate the reason why a request cannot be made"""
  print()
  print(f"{bold(fg_red('Sorry!'))} {bold(fg_red(italic(message)))}")
  input("Press Enter to continue ...\n")
  clear()

# Function to display transaction success message
def display_success_message(message):
  print(f"{bold(fg_green('Order Successfully Completed!'))} {fg_green(italic(message))}")

# Function to display additional message
def display_message(message):
  print(f"{bold(fg_violet(message))}")


