def is_the_list_in_order(my_list):
    # sort the list in order
    index =0
    T=True
    if len(my_list)<=1: T = True
    else:
        while index < len(my_list):
            if my_list[index] <= my_list[index+1]:
                T=True
            else:
                T=False
                break
            index +=1
            if index == len(my_list) - 1: break
    return T
def main():
    print(is_the_list_in_order([1]))
    print(is_the_list_in_order([1]))
main()