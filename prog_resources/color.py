# This module presents colors for which can be used to change colors of texts

# Function to determine item to color
def choose_color(item, color_code):
  background = ["BG", "bg", "bG", "Bg", "Background"]
  foreground = ["FG", "fg", "fG", "Fg", "Foreground"]
  item_code = ""
  if item in background:
    item_code = 48
  elif item in foreground:
    item_code = 38
  else:
    print("Please enter a value for item")
  colored_text = f"\033[{item_code};{5};{color_code}m"
  return colored_text

# Functions for changing foreground (fg) colors
#***(Color Blue)
def fg_blue(text):
  """Makes forecolor blue"""
  colored_text = f"{choose_color('fg',12)}{text}"
  return colored_text

#***(Color Green)
def fg_green(text):
  """Makes forecolor green"""
  colored_text = f"{choose_color('fg',10)}{text}"
  return colored_text

#***(Color Red)
def fg_red(text):
  """Makes forecolor red"""
  colored_text = f"{choose_color('fg',9)}{text}"
  return colored_text

#***(Color yellow)
def fg_yellow(text):
  """Makes forecolor yellow"""
  colored_text = f"{choose_color('fg',11)}{text}"
  return colored_text

#***(Color violet)
def fg_violet(text):
  """Makes forecolor violet"""
  colored_text = f"{choose_color('fg',13)}{text}"
  return colored_text

#***(Color cyan)
def fg_cyan(text):
  """Makes forecolor cyan"""
  colored_text = f"{choose_color('fg',14)}{text}"
  return colored_text
