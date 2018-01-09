#Course_name: Intro to Programming
#Exercise round 03
#project_name: Aquarium
#Name: Phan Viet Anh
#student_number: 256296

def main():
    n = int(input("Enter the number of the measurements: "))
    i = 1
    previous_value = 0
    average_measurement = 0
    total = 0
    if n > 0:
        while 1:
            current_value = float(input("Enter the measurement result " + str(i) + ": "))
            if current_value >= 6 and current_value <= 8:
                if previous_value != 0:
                    if abs(current_value - previous_value) <= 1:
                        total = total + current_value
                        average_measurement = float(total / n)
                    else:
                        print("The conditions are not suitable for zebra fishes.")
                        break
                else:
                    total = total + current_value
                    average_measurement = float(total / n)
            else:
                print("The conditions are not suitable for zebra fishes.")
                break
            i += 1
            previous_value = current_value
            if i > n:
                print("Conditions are suitable for zebra fishes. The average pH is", format(average_measurement, '.2f'))
                break
    else:
        print("Error: the number must be expressed as a positive integer.")

main()
















