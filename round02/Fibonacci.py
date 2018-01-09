def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b
num_in=int(input("How many Fibonacci numbers do you want? "))

for index, fibonacci_number in enumerate(fib()):
  if index!=0 and fibonacci_number!=0:
     print(format(index,'1,.0f'), format(fibonacci_number,'1,.0f'),sep=". ")
     if index == num_in:
         break