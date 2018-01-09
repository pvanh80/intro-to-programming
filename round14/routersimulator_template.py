# Intro to programming
# Routing simulator project
# Phan Viet Anh
# 256296

"""
A program that simulate how the data in the routing tables of routers
are exchanged when devices communicate with each other.
"""


class Router:
    def __init__(self, name):
        """
        Router constructor with a name and neighbor and routing table are empty
        :param name: name of router wish to create
        """
        self.__name = name
        self.__neighbor = []
        self.__routing_table = []

    def print_info(self):
        """ print router info as given format """
        print('  ' + self.__name + '\n'
              + '    N:'
              + ','.join(' ' + neighbor for neighbor in sorted(self.__neighbor))
              + '\n' + '    R:'
              + ','.join(' ' + route for route in sorted(self.__routing_table)))

    def get_name(self):
        """ get name of the router """
        return self.__name

    def get_neighbor(self):
        """ get neighbor of router connect to """
        return self.__neighbor

    def get_routing_table(self):
        """ get routing table of router """
        return self.__routing_table

    def network_list(self):
        """ list of network that router know """
        network = [] # save networks
        for net in self.__routing_table:
            # take the network from route in routing table
            # ie. route=300:0, then network = 300
            network.append(str(net[0:net.index(':'):1]))
        return network

    def add_neighbour(self, router):
        """ add neighbor router when it is not in list of neighbor """
        if router.__name not in self.__neighbor:
            self.__neighbor.append(router.__name)
        pass

    def add_network(self, address, distance):
        """ insert network into routing table """
        network = address + ':' + str(distance)
        self.__routing_table.append(network)
        pass

    def receive_routing_table(self, router):
        """ insert appropriate route into routing table """
        for route in router.__routing_table:
            # check that network in routing table or not
            if str(route[0:route.index(':'):1]) not in self.network_list():
                # distance of network
                distance = int(route[int(route.index(':') + 1):len(route):1]) + 1
                # network address
                address = str(route[0:route.index(':'):1])
                # save route to routing table
                self.add_network(address, distance)

        pass

    def has_route(self, network_name):
        """ Check that network is connected to router or not"""
        # check the network exist in routing table or not
        if network_name not in self.network_list():
            print('Route to the network is unknown.')
        else:
            edge_router = 0  # distance of edge router for the network
            distance = edge_router
            for route in self.__routing_table:
                # network is in route
                if network_name in route:
                    # take the distance of network
                    distance = int(route[int(route.index(':') + 1):len(route):1])
                    break
            if distance == 0:
                print('Router is an edge router for the network.')
            else:
                print('Network ' + network_name + ' is '
                      + str(distance) + ' hops away')

        pass


def read_input_file(file_name):
    """
    read data from file and save to a dict
    :param file_name: name of file want to read data from
    :return: a dict which saved data
    """
    data = {}
    if file_name == '':
        return data
    else:
        file = open(file_name)

        while True:
            line = file.readline().rstrip()  # read line by line
            # end of file
            if line == '':
                break
            # split content into seperate parts (router, neighbor, network)
            result = line.split('!')
            # initialize router object with name of router
            router = Router(result[0])
            # neighbor are not empty
            if result[1] != '':
                # seperate neighbor
                neighbor = result[1].split(';')
                for neighbor_router in neighbor:
                    # save neighbor ot router
                    router.add_neighbour(Router(neighbor_router))
            # networks are not empty
            if result[2] != '':
                # seperate networks
                networks = result[2].split(';')
                for subnet in networks:
                    # check the connected network directly with router when distance = 0
                    if int(subnet[int(subnet.index(':') + 1):len(subnet):1]) == 0:
                        # save network to routing table with network and distance
                        router.add_network(subnet[0:subnet.index(':'):1],
                                           subnet[int(subnet.index(':') + 1):len(subnet):1])
            # save router to dict data
            data[result[0]] = router
        return data


def new_router_command(database):
    """
    Generate router with a name
    :param database: a dict that save routers
    :return: nothing
    """
    router_name = input("Enter a new name: ")
    if router_name not in database:
        database[router_name] = Router(router_name)
    else:
        print('Name is taken.')
    pass


def print_command(database):
    """
    print info as given format
    :param database: a dict that save routers
    :return: nothing
    """
    router_name = input("Enter router name: ")
    if router_name not in database:
        print('Router was not found.')
    else:
        # print info of router
        database[router_name].print_info()
    pass


def connect_command(database):
    """

    :param database:
    :return:
    """
    router1 = input('Enter 1st router: ')
    router2 = input('Enter 2nd router: ')
    # check router are exist or not
    if router1 in database and router2 in database:
            # exchange info to be neighbor
            database[router1].add_neighbour(database[router2])
            database[router2].add_neighbour(database[router1])
    else:
        print('Router was not found.')
        pass


def new_network_command(database):
    """
    create a new network that connect to router
    :param database: a dict that save routers
    :return: nothing
    """
    router_name = input('Enter router name: ')
    network = input('Enter network: ')
    # check distance should be integer
    try:
        distance = int(input('Enter distance: '))
    except:
        print('Distance should be integer.')
    if router_name in database:
        database[router_name].add_network(network, distance)
    else:
        print('Router was not found.')


def print_all(database):
    """
    print all info routers in data
    :param database: a dict that save routers
    :return: nothing
    """
    for router in sorted(database):
        database[router].print_info() # print info of router
    pass


def send_command(database):
    """
    exchange routing table to its neighbor
    :param database: a dict that save routers
    :return: nothing
    """
    router_name = input("Sending router: ")
    for neighbor in database[router_name].get_neighbor():
        # each neighbor of the router should receive appropriate route
        database[neighbor].receive_routing_table(database[router_name])
    pass


def route_request(database):
    """
    Check that the distance between router and requested network
    :param database: a dict that save routers
    :return: nothing
    """
    router_name = input('Enter router name: ')
    network_name = input('Enter network name: ')
    # whether router has the route with network or not
    # print distance between router and network
    database[router_name].has_route(network_name)

    pass


def main():

    routerfile = input("Network file: ")
    try:
        database = read_input_file(routerfile)

        while True:
            command = input("> ")
            command = command.upper()

            if command == "P":
                print_command(database)
                pass

            elif command == "PA":
                print_all(database)
                pass

            elif command == "S":
                send_command(database)
                pass

            elif command == "C":
                connect_command(database)
                pass

            elif command == "RR":
                route_request(database)
                pass

            elif command == "NR":
                new_router_command(database)
                pass

            elif command == "NN":
                new_network_command(database)
                pass

            elif command == "Q":
                print("Simulator closes.")
                return

            else:
                print("Erroneous command!")
                print("Enter one of these commands:")
                print("NR (new router)")
                print("P (print)")
                print("C (connect)")
                print("NN (new network)")
                print("PA (print all)")
                print("S (send routing tables)")
                print("RR (route request)")
                print("Q (quit)")
    except:
        print('Error: the file could not be read or there is something wrong with it.')

main()
