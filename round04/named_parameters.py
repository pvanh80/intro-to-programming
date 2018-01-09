# Introduction to Programming
# Named parameters
# Default value of function arguments will be used if some of arguments is not appear in the function call
def print_box(width, height, border_mark="#", inner_mark=" "):
  for i in range(height):
    if i==0 or i==height-1:
      print(width*border_mark)
    else:
      print(str(border_mark) + (width-2)*str(inner_mark) + str(border_mark) )
  print()
def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

main()

