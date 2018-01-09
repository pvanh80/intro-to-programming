def increasing_list(n):
  i=0
  while i<=n :
    if i%2==0:
      print(i)
    i+=1
def decreasing_list(n):
  i=n
  while i>=0 :
    if i%2==0:
      print(i)
    i-=1
def main():
  n=100
  increasing_list(n)
  decreasing_list(n)
main()