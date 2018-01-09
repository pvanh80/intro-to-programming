# intro to programming
# Closure
# Phan Viet Anh
# 256296

def create_a_multiplier(n):
    def multiplier(x):
        return n*x
    return multiplier


def create_a_counter():
    count = 1
    def counter():
        nonlocal count
        total = count
        count += 1
        return total
    return counter

#
# def create_a_counter():
#     next_value = 1
#     def return_next_value():
#         nonlocal next_value
#         val = next_value
#         next_value += 1
#         return val
#     return return_next_value

def main():
    # doubler = create_a_multiplier(2)
    #
    # print(doubler)
    # print(doubler(2))
    # print(doubler(3))
    #
    # tripler = create_a_multiplier(3)
    #
    # print(tripler)
    # print(tripler(2))
    # print(tripler(3))
    #
    # print(doubler(2))
    first_counter = create_a_counter()
    second_counter = create_a_counter()
    print(first_counter())
    print(second_counter())
    print(first_counter())
    print(first_counter())
    print(second_counter())


main()
