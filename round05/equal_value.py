def are_all_members_same(my_list):
    index = 0
    T=True
    while index < len(my_list):
        if my_list[index] == my_list[index - 1]:
            T=True
        else:

            T= False
            break
        index += 1
        # if index>=len(my_list): break
    return T

def main():
    print(are_all_members_same([42, 42, 42, 43, 42]))
    print(are_all_members_same([42, 42, 42, 42, 42]))


main()