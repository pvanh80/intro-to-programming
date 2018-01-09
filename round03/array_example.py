def num(s):
    return int(s)


n_measurement = input('Enter number of measurement: ')
i = 1
data_measurement = ""
while i <= n_measurement:
    x = input('Enter the result number '+ str(i) + ': ')
    if x >=6 and x<=8:
        if i!=n_measurement:
            data_measurement += str(x) + ','
        else:
            data_measurement += str(x)
        list_measurement = data_measurement.split(",")
        results = list(map(int, list_measurement))
        for j in range(n_measurement):
            if results[j] - results[j-1] < 1:
                i += 1
            else:
                print("Not suitable value")
                break

    else:
        print("Not suitable value")
        break

for e in list_measurement:
    print(e)

#solution nnumber 2:

#Course_name: Intro to Programming
#Exercise round 03
#project_name: Aquarium
#Name: Phan Viet Anh
#student_number: 256296

from array import *

def main():
    result_of_measurements = array('f', [])
    i = 0
    average_ph = 0
    total = 0
    n_measurements = int(input("Enter the number of the measurements: "))
    if n_measurements > 0:
        while 1:
            x = float(input("Enter the measurement result " + str(i + 1) + ": "))
            if x >= 6 and x <= 8:
                result_of_measurements.append(x)
                if result_of_measurements[i] - result_of_measurements[i - 1] > 1 or result_of_measurements[i] - \
                        result_of_measurements[i - 1] < -1:
                    print("The conditions are not suitable for zebra fishes.")
                    break

                else:
                    total += result_of_measurements[i]
                    average_ph = total / n_measurements
                    i += 1
            else:
                print("The conditions are not suitable for zebra fishes.")
                break
            if i >= n_measurements:
                print ("Conditions are suitable for zebra fishes. The average pH is", format(average_ph,'.2f'))
                break
    else:
        print("Error: the number must be expressed as a positive integer.")


main()

#Solution number 3
mylist = ""
n = int((input("Number of results: ")))
i = 1
while i <= n:
    x = float(input("Enter " + str(i) + " :"))
    if x >= 6 and x <= 8:
        if i != n:
            mylist += str(x) + ","
        else:
            mylist += str(x)

        i += 1
    else:
        print("No good value")
        break
print(mylist)
results = [float(y) for y in mylist.split(",")]
for j in range(len(results)):
    if results[j] - results[j - 1] > 1:
        print("No good value")
        break

















