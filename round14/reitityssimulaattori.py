
def main():

    network_file = input("Network file: ")

    while True:
        command = input("> ")
        command = command.upper()

        if command == "T":  # TODO: Organize the final order of the assignment
            pass
        
        elif command == "TK":
            pass

        elif command == "L":
            pass

        elif command == "Y":
            pass

        elif command == "R":
            pass

        elif command == "UR":
            pass

        elif command == "UV":
            pass

        elif command == "Q":
            print("The simulator is closed.")
            return

        else:
            print("Invalid command!")
            print("Enter one of the following commands:")
            print("UR (new router)")
            print("T (tiedot)")  # TODO: Järjestetään tehtävänannon lopulliseen järjestykseen
            print("Y (reitittimien yhdistäminen)")
            print("UV (uusi verkko)")
            print("TK (kaikkien tiedot)")
            print("L (reititystaulujen lähetys)")
            print("R (reittikysely)")
            print("Q (lopeta)")

main()
