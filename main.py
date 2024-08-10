from prog_resources.color import *
from prog_resources.format import *
from prog_resources.art import *
# from prog_resources.coffee_items import *
from prog_resources.operations import *

# Declare module variable 
amount_paid = 0



# Assign welcome greetings to a variable
greetings = "Welcome to Loraperz Breweries"
print(f"\n{bold(underline(fg_green(greetings)))}\n")

# Print company logo
print(f"{bold(fg_green(logo))}")

operate_machine = True
while operate_machine:
  # Prompt the user to choose an operation
  operation_option = int(input(f"Choose from the following to perform the corresponding operations:\n\t1. Put Coffee Machine Off\n\t2. Print Report on Resources\n\t3. Serve a customer: {format_input_text()} "))

  if operation_option == 1:
    put_coffee_machine_off()
  elif operation_option == 2:
    print_report()
  elif operation_option == 3:
    # Prompt the user to enter what the client wishes to take
    coffee_chosen = input(f"\nWhat would you like? espresso/latte/cappuccino: {format_input_text()}")
    if is_resources_sufficient(coffee_chosen):
      # Prompt user to insert coins
      print(f"\nEnter coins to make payment for your coffee.")
      quarters_amount = int(input(f"How many quarters?:{format_input_text()}"))
      dimes_amount = int(input(f"How many dimes?:{format_input_text()}"))
      nickles_amount = int(input(f"How many nickels?:{format_input_text()}"))
      penny_amount = int(input(f"How many pennies?:{format_input_text()}"))
      amount_paid = calculate_payment(quarters_amount, dimes_amount, nickles_amount, penny_amount)

          # Determine if amount paid is sufficient
      if is_payment_sufficient(coffee_chosen, amount_paid):
        make_coffee(coffee_chosen)  # Deduct resources used to prepare the coffee chosen and add revenue earned to money
        print("\n***********************************")
        display_success_message(f"Take your {coffee_chosen}.")
        display_message(f"\nYour coffee costs {get_coffee_cost(coffee_chosen)}.")
        display_message(f"You paid {format_amount(amount_paid)}.")
        display_message(give_change(coffee_chosen, amount_paid))
        print("***********************************")
      else:
        sorry_message = f"You did not pay enough to prepare the coffee ({coffee_chosen}) you requested."
        display_sorry_message(sorry_message)
        print("")
    else:
      sorry_message = f"There are not enough resources to prepare the coffee ({coffee_chosen}) you requested."
      display_sorry_message(sorry_message)

  # Prompt the user to choose whether to continue or not
  continue_operation = input(f"\nDo you want to continue? 'y' or 'n': {format_input_text()}")
  if continue_operation == 'n':
    operate_machine = False
    clear()
    display_message("\nThank you for using Loraperz Breweries Coffee Machine. Have a nice day!\n")
  elif continue_operation == 'y':
    operate_machine = True
    clear()
  else:
    print("Enter 'y' or 'n' to continue or not")