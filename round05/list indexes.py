def read_number(promt,errormessage="Incorrect input: "):
  try:
    return float(input(promt))
  except ValueError as e:
    print(errormessage)
    return read_number(promt,errormessage)
    
    
def in_list(n):
  Number=[]
  print('Give '+ str(n) +' numbers: ')
  i=0
  while i<5:
    x = read_number("Next number: ")
    Number.append(x)
    i+=1 
  return Number  
    
def print_reverse(number):
  i = len(number) - 1
  while i>=0:
   print(format(number[i],'.0f'))
   i-=1
      
      
def main():
  n = 5
  a = in_list(n)
  print("The numbers you entered, in reverse order:")
  print_reverse(a)
main()




















