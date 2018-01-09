# Course_name: Intro to Programming
# Exercise round 06
# project_name: Coffee Gallup
# Name: Phan Viet Anh
# Student_number: 256296

"""

Finnish people drink too much coffee. The authorities are concerned and decided
to investigate the situation by arranging a gallup to find out some accurate numbers.

Gallup asks each passing person, how many cups of coffee, they drink on a daily basis
and writes down the response. Implement a program that conducts some calculations for
the responses

"""


def most_respondent(result):
    """
    This function find out the most respondent coffee in Gallup
    by sorting increasingly the number of appearance of respondent

    # parameters:
    #       result: a list of respondent in coffee gallup
    # return: the last element in the list

    """
    index = 0  # No. index
    while index < len(result):

        if result.count(result[index]) <= result.count(result[index - 1]):
            result[index], result[index - 1] = result[index - 1], result[index]

        index += 1

    return result[len(result) - 1]


def less_and_greater_most_res(result):
    """
    This function calculates the number of respondent drinks from
    less to greater than the most coffee respondent 1 cups coffee
    per day, not print out anything

    # parameters:
    #       result: a list of respondent in coffee gallup
    # return: the percentage of respondent 4 - 6 cup in gallup

    """

    num_cups_coffee = most_respondent(result)
    less_one_cup = num_cups_coffee - 1
    greater_one_cup = num_cups_coffee + 1

    num_respondent = 0

    # respondent drinks less or greater than 1 cups coffee per day compared to
    # the most respondent
    coffee_intake_range = (less_one_cup, num_cups_coffee, greater_one_cup)

    for index in range(len(result)):

        if result[index] in coffee_intake_range:
            num_respondent += 1

    return num_respondent


def more_four_cup(result):
    """
    This function calculate the number of respondent drinks more than
    4 cups coffee per day, not print out anything

    # parameters:
    #       result: a list of respondent in coffee gallup
    # return: the percentage of respondent more than 4 cups in gallup

    """
    num_gre_fourth_cup = 0
    coffee_intake = 4  # respondent drinks 4 cups coffee per day

    for index in range(len(result)):

        if result[index] > coffee_intake:
            num_gre_fourth_cup += 1

    return num_gre_fourth_cup


def drink_little_much(result):
    """
    This function counts the number of respondent drinks 5 - 8 cups coffee
    per day, not print out anything

    # parameters:
    #       result: a list of respondent in coffee gallup
    #return: the percentage of respondent drink 5 - 8 cups in gallup

    """
    num_res_too_much = 0
    coffee_intake_range = [5, 6, 7, 8]  # respondent drinks 5 - 8 cups coffee per day

    for index in range(len(result)):

        if result[index] in coffee_intake_range:
            num_res_too_much += 1

    return num_res_too_much


def drink_over_double_rec(result):
    """
    This function calculates the number of respondent drinks over 8 cups
    coffee per day, not print out anything

    # parameters:
    #       result: a list of respondent in coffee gallup
    # return: the number of respondent drinks over 8 cups coffee

    """
    num_over_double_rec = 0
    recommended_intake = 8  # respondent drinks over 8 cups

    for index in range(len(result)):

        if result[index] > recommended_intake:
            num_over_double_rec += 1

    return num_over_double_rec


def list_res_over_rec(result):
    """
    This function is making a list that respondent drink over double coffee
    intake recommendation coffee per day (2 x 4 cups), not print out anything

    # parameters:
    #       result: a list of respondent in coffee gallup
    # return: a list contains respondent drink over double recommendation intake

    """
    list_over_double_rec = []
    recommended_intake = 8  # respondent drinks over double recommendation cups

    for index in range(len(result)):

        if result[index] > recommended_intake:
            list_over_double_rec.append(result[index])

    return list_over_double_rec


def remove_zero(result):
    """
    This function just remove non-coffee-drinkers out of list respondent
    coffee gallup, not print out anything
    # parameters:
    #       result: a list of respondent in coffee gallup
    # return: a list without non-coffee-drinkers
    """
    non_coffee_drinkers = 0
    result_temp = []

    for index in range(len(result)):

        if result[index] > non_coffee_drinkers:
            result_temp.append(result[index])

    return result_temp


def print_info_drinkers(result):
    """
    Printing info list of respondent coffee Gallup with
    known format (2-character-wide column)

    # parameters
            result:

    """
    result.sort()
    mark = "#"
    index = min(result)  # j index run from minimum of list respondent

    while index <= max(result):

        print(str(format(index, '2.0f')) + ' ' + result.count(index) * mark)

        index += 1


def main():

    list_result = []  # List of respondent coffee Gallup

    print("Enter one response per line. End by entering an empty row.")

    while True:

        correspondent = input("")  #

        if str(correspondent) == "":
            break

        else:
            try:
                data = int(correspondent)  # respondent from user input

                if data >= 0:
                    list_result.append(data)

                else:
                    print("Error: Wrong Value.!")

            except ValueError:
                print("Error: Wrong Value. Input should be integer !")
    # List of respondent coffee gallup after removing non-coffee-drinkers
    list_result_after = remove_zero(list_result)

    # Number of non-coffee-drinkers are removed out of list respondent
    nums_non_coffee_drinker = len(list_result) - len(list_result_after)

    # List of coffee respondent drink over recommendation intake
    result_over_recommend = list_res_over_rec(list_result_after)

    # Print notification when the list contains non-coffee-drinkers
    if nums_non_coffee_drinker > 0:
        print("Removed " + str(nums_non_coffee_drinker) +
              " non-coffee-drinkers responses")

    # Print out info result of Coffee Gallup when respondents are available
    if len(list_result_after) > 0:

        print("\nInformation related to coffee drinkers:")

        # print out information related to coffee drinkers
        print_info_drinkers(list_result_after)

        # Print out the greatest respondent in Coffee Gallup
        print("\nThe greatest response: " + str(max(list_result_after)) +
              " cups of coffee per day")

        # Print out the most common respondent in Coffee Gallup
        print("The most common response: "
              + str(most_respondent(list_result_after)) +
              " cups of coffee per day")

        # respondent drinks less or greater than 1 cups coffee per day compared to
        # the most respondent
        num_cups_coffee = most_respondent(list_result_after)
        less_one_cup = num_cups_coffee - 1
        greater_one_cup = num_cups_coffee + 1

        num_res_les_gre = float(less_and_greater_most_res(list_result_after)
                                / len(list_result_after)*100)

        # Print out the number of respondent drinker 4-6 cups per day
        print(str(format(num_res_les_gre, '.1f')) +
              "% of the respondents drink " + str(less_one_cup) + "-" +
              str(greater_one_cup) + " cups of coffee per day")

        # Number of respondent drink more than four cups per day
        num_more_four = more_four_cup(list_result_after)

        if num_more_four > 0:

            print("\nInformation related to coffee abusers:")

            #
            num_gre_four_cup = float(more_four_cup(list_result_after) /
                                     len(list_result_after)*100)

            # Print out % of the respondents drink more than 4 cups coffee per day
            print(str(format(num_gre_four_cup, '.1f')) +
                  "% of the respondents drink more than 4 cups of coffee per day")

            # Print out respondents drink 5-8 cups coffee per day
            print(str(drink_little_much(list_result_after)) +
                  " respondents drink a little too much coffee (5-8 cups per day)")

            # Print out respondents drink over double the recommendation
            print(str(drink_over_double_rec(list_result)) +
                  " respondents drink over double the recommendation")

        # Number of respondent drink over recommendation intake
        num_over_double_rec = drink_over_double_rec(list_result_after)

        if num_over_double_rec > 0:

            print("The responses over 8 cups of coffee per day: ")

            # Print out list respondent drink over 8 cups coffee per day
            for element in result_over_recommend:
                print(element)


main()
