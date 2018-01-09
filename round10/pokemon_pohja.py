# intro to programming
# Pokemon
# Phan Viet Anh
# 256296

# This dict is a global constant, that will be used to determine the
# effects of the Pokémon attacks. The keys of this dict are Pokémon types. 
# The values related to the keys are dicts, where the keys are attack types
# and values are the effect factors of the attacks.
# For example, a Ghost-type attack of a Normal-type Pokémon causes 0.8* harm
# and a Fighting-type attack of the same Pokémon causes 1.25* harm.
TYPES = {"Normal": {"Fighting": 1.25, "Ghost": 0.8},
         "Fighting": {"Flying": 1.25, "Psychic": 1.25, "Fairy": 1.25,
                      "Rock": 0.8, "Bug": 0.8, "Dark": 0.8},
         "Flying": {"Electric": 1.25, "Rock": 1.25, "Ice": 1.25, "Grass": 0.8,
                    "Bug": 0.8, "Fighting": 0.8, "Ground": 0.8},
         "Poison": {"Ground": 1.25, "Psychic": 1.25, "Fighting": 0.8,
                    "Bug": 0.8, "Poison": 0.8, "Grass": 0.8, "Fairy": 0.8},
         "Ground": {"Water": 1.25, "Grass": 1.25, "Ice": 1.25, "Poison": 0.8,
                    "Rock": 0.8, "Electric": 0.8},
         "Rock": {"Fighting": 1.25, "Ground": 1.25, "Steel": 1.25,
                  "Water": 1.25, "Grass": 1.25, "Normal": 0.8, "Flying": 0.8,
                  "Poison": 0.8, "Fire": 0.8},
         "Bug": {"Flying": 1.25, "Rock": 1.25, "Fire": 1.25, "Fighting": 0.8,
                  "Ground": 0.8, "Grass": 0.8},
         "Ghost": {"Ghost": 1.25, "Dark": 1.25, "Bug": 0.8, "Poison": 0.8,
                    "Normal": 0.8, "Fighting": 0.8},
         "Steel": {"Fighting": 1.25, "Ground": 1.25, "Fire": 1.25,
                    "Normal": 0.8, "Flying": 0.8, "Rock": 0.8, "Bug": 0.8,
                    "Steel": 0.8, "Grass": 0.8, "Psychic": 0.8, "Ice": 0.8,
                    "Dragon": 0.8, "Fairy": 0.8, "Poison": 0.8},
         "Fire": {"Ground": 1.25, "Rock": 1.25, "Water": 1.25, "Bug": 0.8,
                   "Steel": 0.8, "Fire": 0.8, "Ice": 0.8, "Fairy": 0.8},
         "Water": {"Grass": 1.25, "Electric": 1.25, "Steel": 0.8, "Fire": 0.8,
                    "Water": 0.8, "Ice": 0.8},
         "Grass": {"Flying": 1.25, "Poison": 1.25, "Bug": 1.25, "Fire": 1.25,
                    "Ice": 1.25, "Ground": 0.8, "Water": 0.8, "Grass": 0.8,
                    "Electric": 0.8},
         "Electric": {"Ground": 1.25, "Flying": 0.8, "Steel": 0.8,
                       "Electric": 0.8},
         "Psychic": {"Bug": 1.25, "Ghost": 1.25, "Dark": 1.25, "Fighting": 0.8,
                      "Psychic": 0.8},
         "Ice": {"Fighting": 1.25, "Rock": 1.25, "Steel": 1.25, "Fire": 1.25,
                  "Ice": 1.25},
         "Dragon": {"Ice": 1.25, "Dragon": 1.25, "Fairy": 1.25, "Fire": 0.8,
                     "Grass": 0.8, "Water": 0.8, "Electric": 0.8},
         "Dark": {"Fighting": 1.25, "Bug": 1.25, "Fairy": 1.25, "Ghost": 0.8,
                   "Psychic": 0.8},
         "Fairy": {"Poison": 1.25, "Steel": 1.25, "Fighting": 0.8, "Bug": 0.8,
                    "Dark": 0.8, "Dragon": 0.8}}


def factor(attack_type, pokemon_type):
    """
    Finds the effectiveness factor of an attack from the above defined 
    datastructure.
    :param attack_type: String
    :param pokemon_type: String
    :return: Returns the effectiveness factor of the attack
    """
    if pokemon_type in TYPES:

        if attack_type in TYPES[pokemon_type]:
            return TYPES[pokemon_type][attack_type]

    return 1


class Pokemon:
    """ Implements one Pokémon that has a name, types, hitpoints, level 
    and moves."""

    def __init__(self, species, types, hp=50, level=20):
        """
        Constructor of the class. Checks the kesto and level and stores
        the attributes.

        :param species: the species of the pokemon
        :param types:   the types of the pokemon
        :param hp:      the hp of the pokemon
        :param level:   the level of the pokemon
        """

        self.__species = species.capitalize()
        self.__types = types

        if not isinstance(hp, int) or not isinstance(level, int) \
                or hp < 0 or level < 1:
            raise ValueError

        self.__hp = hp
        self.__max_hp = hp
        self.__level = level
        self.__moves = {}

    def info(self):
        """
        Prints information in the form of species, types, hp.
        """
        print(self.__species, ", ", self.__hp, "hp", ", Types: ",
              ", ".join(self.__types), sep="")
        print()

    def heal(self, hp):
        try:

            if int(hp) > 0:
                if int(hp) + self.__hp > self.__max_hp:
                    self.__hp = self.__max_hp
                else:
                    self.__hp += int(hp)
                print(str(self.__species) + ' was healed ' + str(hp) + ' hp')

                return True
            else:
                return False
        except:
            return False

    def damage(self, damage):
        try:
            if int(damage) > 0:
                if int(damage) >= self.__hp:
                    print(str(self.__species) + ' lost ' + str(self.__hp) + ' hp')
                    print(str(self.__species) + ' fainted!')
                    self.__hp = 0
                else:
                    self.__hp -= int(damage)
                    print(str(self.__species) + ' lost ' + str(damage) + ' hp')

                return True
            else:
                return False
        except:
            return False

    def set_types(self, pokemon_type):
        """

        :param pokemon_type: a list of pokemon type
        :return: boolean value
        """

        for index in range(len(pokemon_type)):
            if pokemon_type[index].capitalize() not in TYPES:
                return False
                break
            else:
                pokemon_type[index] = pokemon_type[index].capitalize()
        self.__types = pokemon_type
        return True

    def add_type(self, pokemon_type):
        if pokemon_type.capitalize() not in TYPES:
            return False
        else:
            self.__types.append(pokemon_type.capitalize())
            return True

    def add_move(self, move_name, power, move_type):
        #return len(self.__moves)
        if len(self.get_moves()) > 2:
            return False
        elif move_type not in TYPES:
            return False

        else:
            power_and_move_type = [power, move_type]
            self.__moves[move_name.title()] = power_and_move_type
            return True

    def move_info(self):
        print(str(self.__species) + '\'s moves: ')
        for move in self.__moves:
            print(move, self.__moves[move][0], self.__moves[move][1], sep=', ')
        print()

    def attack(self, move_name, pokemon_enemy):
        EFFECTIVE = 1.25
        INEFFECTIVE = 0.8
        FOUND = 0
        total_rate_damege = 1
        attack_power = self.__moves[move_name.title()][0]
        attack_type = self.__moves[move_name.title()][1]
        real_hp_lost = 0
        if self.__hp != 0:
            print(str(self.__species) + ' used ' + move_name.title() + '.')

            for type_effect in pokemon_enemy.__types:
                if attack_type in TYPES[type_effect]:
                    total_rate_damege *= TYPES[type_effect][attack_type]
                    FOUND +=1

                    #break
            if TYPES[type_effect][attack_type] == 0.8:
                print('It\'s not very effective.')
            else:
                print('It\'s super effective!')
            real_hp_lost = attack_power * total_rate_damege
            hp_lost = pokemon_enemy.__hp - real_hp_lost

            if hp_lost <= 0:
                print(str(pokemon_enemy.__species) + ' lost '
                      + str(int(pokemon_enemy.__hp)) + ' hp.')
                print(str(pokemon_enemy.__species) + ' fainted!')
                pokemon_enemy.__hp = 0
                return True
            else:
                pokemon_enemy.__hp -= real_hp_lost
                print(str(pokemon_enemy.__species) + ' lost '
                      + str(int(real_hp_lost)) + ' hp.\n')
                return True
        else:
            print('Pokemon has fainted and can\'t attack.')
            return False

    def get_moves(self):
        return self.__moves

def main():


    pikachu = Pokemon("Pikachu", ["Electric"])
    pikachu.info()
    print(pikachu.set_types(['dark', 'POIson']))
    pikachu.info()
    pikachu.damage(10)
    pikachu.info()
    pikachu.heal(90)
    pikachu.info()
    pikachu.add_move("Thundershock", 50, "Electric")
    pikachu.add_move("Thundershock", 50, "Electric")
    pikachu.add_move("TACKLE", 30, "Normal")
    pikachu.add_move("Quick Attack", 40, "Normal")
    pikachu.move_info()
    print(len(pikachu.get_moves()))
    # rattata = Pokemon("Rattata", ["Normal"])
    #
    # pikachu.add_move("TACKLE", 30, "Normal")
    # pikachu.add_move("Thundershock", 50, "Electric")
    #
    # rattata.add_move("Quick Attack", 40, "Normal")
    #
    # pikachu.attack("Tackle", rattata)
    #
    # rattata.attack("Quick ATTACK", pikachu)
    #
    # pikachu.attack("Thundershock", rattata)
    #
    # rattata.attack("Quick ATTACK", pikachu)

    # mew = Pokemon("Mew", ["Psychic"], 100, 40)
    # gyarados = Pokemon("Gyarados", ["Water", "Flying"], 200, 60)
    # mew.info()
    # gyarados.info()
    #
    # mew.add_move("Earthquake", 100, "Ground")
    #
    # mew.add_move("Thunderbolt", 90, "Electric")
    #
    # gyarados.add_move("Splash", 0, "Normal")
    #
    # mew.move_info()
    #
    # gyarados.move_info()
    #
    # mew.attack("Earthquake", gyarados)
    # mew.attack("Thunderbolt", gyarados)
    #
    #
    # gyarados.attack("Splash", mew)


main()