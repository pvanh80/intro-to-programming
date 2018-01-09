# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task auto_luokkana, program code template

MENU_TEXT =  "1) Fill 2) Drive 3) Quit \n-> "
CAR_TEXT = "The tank contains {:.1f} liters of gas and " + \
           "the odometer shows {:.1f} kilometers."


# Class Car: Implements a car that moves a certain distance and can be 
# filled. The class defines what is the car like: what information it 
# contains and what operations can be carried out for it.
class Car:
    
    # Method: constructor, initiates the object (tank is empty and 
    # location is 0, 0)
    # Parameter: tank_size, the size of this car's tank
    # Parameter: gas_consumption, how much gas this car consumes when it
    #            drives a 100 kilometers 
    def __init__(self, tank_size, gas_consumption):
        self.__tank_size = tank_size
        self.__gas_consumption = gas_consumption
        self.__gas = 0
        self.__odometer = 0

    # TODO: Insert here the definitions of all other methods of this class.
    # The methods are a part of the class. Therefore, they are intended on 
    # this level (=inside the class definition).

    def set_tanksize(self, tanksize):
        self.__tank_size = tanksize

    def set_gas_consumption(self, gas_consumption):
        self.__gas_consumption = gas_consumption

    def set_gas(self, gas):
        self.__gas = gas

    def set_odometer(self, odometer):
        self.__odometer = odometer

    def get_tank_size(self):
        return self.__tank_size

    def get_gas_consumption(self):
        return self.__gas_consumption

    def get_gas(self):
        return self.__gas

    def get_odometer(self):
        return self.__odometer

    def printInformation(self):

        print('The tank contains ' + format(self.__gas, '.1f')
              + ' liters of gas and the odometer shows '
              + format(self.__odometer, '.1f')
              + ' kilometers')
    
def main():

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas_consumption = read_number("How many liters of gas does the car " + \
                                  "consume per hundred kilometers? ")
    
    # Here we define the variable car which is an object initiated from the
    # class Car. This is the line where the constructor of the class Car
    # (the method that is named __init__) is called!
    car = Car(tank_size, gas_consumption)
    
    # (In this program we only need one car-object but it is possible
    # to create multiple objects from one class. For example we could
    # create two objects:
    # lightning_mcqueen = Car(20, 30)
    # mater = Car(10, 10) )

    while True:
        car.printInformation()
        choice = input(MENU_TEXT)
        if choice == "1":
           to_fill = read_number("How many liters of gas to fill up? ")
           # TODO: call the fill-method for the car-object here (task b)

        elif choice == "2":
           distance = read_number("How many kilometers to drive? ")
           # TODO: call the drive-method for the car-object here (task c)

        elif choice == "3":
           break
    print("Thank you and bye!")


def read_number(prompt, error_message="Incorrect input!"):

    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError as e:
        print(error_message)
        return read_number(prompt, error_message)


main()
