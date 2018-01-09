# Intro to programming
# Numerical integration
# Phan Viet Anh
# 256296
# http://mathworld.wolfram.com/RiemannSum.html


def math_function(x):
    return -pow(x,2) + 2*x + 4

def approximate_area(math_function, lower_bound_area, upper_bound_area, number_rec):
    step = (upper_bound_area-lower_bound_area)/number_rec
    area = 0
    index = 1
    for index in range(0,number_rec):
        area += min(math_function(lower_bound_area + (index * step)),
                    math_function(lower_bound_area + ((index + 1) * step))) * step

    return area

# Riemann Sum with additional parameter sample_type: lower, upper, middle point,
# def approximate_area(math_function, lower_bound_area, upper_bound_area, number_rec, sample_type):
#     step = (upper_bound_area-lower_bound_area)/number_rec
#     area = 0
#     index = 1
#     for index in range(0,number_rec):
#         area += min(math_function(lower_bound_area + (index * step)),
#                     math_function(lower_bound_area + ((index + 1) * step))) * step
#
#     return area


def main():
    print(approximate_area(math_function, -1, 3, 4))

main()
