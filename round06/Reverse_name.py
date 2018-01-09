
def reverse_name(string_input):
    result = ''
    if string_input.count(',') == 0:
        result = string_input
    elif string_input.count(',') == 1:
        b = string_input.split(",")
        if len(b) > 1:
            b.reverse()
            for e in b:
                result += e.strip()
                result += ' '
        else: result = string_input
    return result.strip()

def main():
    a = "Hello,"
    print(reverse_name(a))
main()

