def calculate_angle(a,b=None):
  if b==None:
    return float(90-a)
  else:
    angle = float(180-a-b)
    return angle

def main():
  print(format(calculate_angle(50,60),'.0f'))
  print(format(calculate_angle(30),'.0f'))
main()