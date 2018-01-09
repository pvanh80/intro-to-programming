# intro to programming
# Nested Function
# Phan viet anh
#256296

def sum(a,b):
    def multiply(a,b):
        return a*b
    return multiply(a,b) + multiply(a,b)

def main():
    print(sum(3,4))
main()