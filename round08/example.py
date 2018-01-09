

def main():
    customer = open("customer.txt", 'r')
    #name = "Phan Viet Anh\nHoang The Anh"
    name=customer.read()
    print(name)
    customer.close()


main()