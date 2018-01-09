# Johdatus ohjelmointiin
# Area
from math import sqrt

def area(s1, s2, s3):
    s_half = (s1 + s2 + s3) / 2
    area_tri = sqrt(s_half * (s_half - s1) * (s_half - s2) * (s_half - s3))
    return area_tri

def main():
    rivi1 = float(input("Enter the length of the first side: "))
    rivi2 = float(input("Enter the length of the second side: "))
    rivi3 = float(input("Enter the length of the third side: "))

    print("The triangle's area is ", format(area(rivi1, rivi2, rivi3), '.1f'))

main()
