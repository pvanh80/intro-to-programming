def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def lottery_rows_exist(lottery_balls, drawn_balls):
    numerator = factorial(lottery_balls)
    denominator = factorial(lottery_balls - drawn_balls) * factorial(drawn_balls)
    return numerator / denominator


def main():
    n_balls = int(input("Enter the total number of lottery balls: "))
    n_drawn_balls = int(input("Enter the number of the drawn balls: "))
    if n_balls > 0 and n_drawn_balls > 0:
        if n_drawn_balls < n_balls:
            print("The probability of guessing all "+ str(n_drawn_balls) + " balls correctly is " + '1/',
              format(lottery_rows_exist(n_balls, n_drawn_balls), '.0f'), sep="")
        else:
            print("At most the total number of balls can be drawn.")
    else:
        print("The number of balls must be a positive number.")


main()