def compare_floats(a, b, EPSILON):
    if abs(a-b)<EPSILON:
        return True
    else: return False
EPSILON = 0.000000001
print(compare_floats(0.00000000000000000001, 0.0000000000000000002, EPSILON))
print(compare_floats(0.0002, 0.0000002, EPSILON))