def read_number(promt,errormessage="Incorrect input: "):
  try:
    return float(input(promt))
  except ValueError as e:
    print(errormessage)
    return read_number(promt,errormessage)
def print_less_zero(number):
  for i in number:
    if i>0:
      print(format(i, '.0f'))
def main():
  Number=[]
  print("Give 5 numbers: ")
  i=0
  while i<5:
    x = read_number("Next number: ")
    Number.append(x)
    i+=1  
  print("The numbers you entered that were greater than zero were:")
  print_less_zero(Number)
main()