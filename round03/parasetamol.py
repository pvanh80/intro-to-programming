# Johdatus ohjelmointiin
# Parasetamol

def calculate_dose(weight, time, ratio):
    total = 4000
    amount_base_w = weight*15
    amount_time = time/6
    if amount_time < 1:
        return 0
    else:
        if total - ratio > amount_base_w:
            return amount_base_w
        else :
            return total - ratio



def main():

    w = float(input("Patient's weight (kg): "))
    t = float(input("How much time has passed from the previous dose (full hours): "))
    r = float(input("The total dose for the last 24 hours (mg): "))
    print("The amount of Parasetamol to give to the patient: ", format(calculate_dose(w,t,r),'.0f'))

main()
