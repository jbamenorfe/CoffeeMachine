# Import dependant files
import os
from prog_resources.color import *

# Define a function to clear the console
def clear():
  os.system('cls')

def exit():
  os._exit(1)

def clear_to_text(text):
  print('\033c')
  print(f"{text}")

# Function to clear formatting
def clearFormat():
  return f"{''}\033[0m"

# Function to format text bold
def bold(text):
  bolded_text = f"\033[1m{text} {clearFormat()}"
  return bolded_text

# Function to format text italicise
def italic(text):
  italicised_text = f"\033[3m{text} {clearFormat()}"
  return italicised_text

# Function to format text underline
def underline(text):
  underlined_text = f"\033[4m{text} {clearFormat()}"
  return underlined_text

# OTHER IMPORTANT FUNCTIONS
def format_input_text():
  """Returns the input made by user after changing it to color green"""
  return f"\n\t{bold(fg_green('-->: '))}"

def display_Result(num1, num2, operator, answer):
  """Takes in num1, num2, operator, answer formats them and prints them to the console"""
  result = f"RESULTS:\n`````````\n{num1} {operator} {num2} = {answer:,.2f}\n========================"
  print(f"{bold(fg_blue(result))}")
  clearFormat()