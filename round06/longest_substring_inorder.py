def longest_substring_in_order(s):
    groups = []
    cur_longest = ''
    prev_char = ''
    for c in s.lower():
        if prev_char and c < prev_char:
            groups.append(cur_longest)
            cur_longest = c
        else:
            cur_longest += c
        prev_char = c
    return groups  # if groups else s

"""
    j = 0
    while j < len(list_str):

        if len(list_str[j]) <= len(list_str[j - 1]):
            list_str[j], list_str[j - 1] = list_str[j - 1], list_str[j]

        j += 1

    long_substring = list_str[len(list_str) - 1]
    """
def main():
    print(longest_substring_in_order("efghijklmnopopqefgabcdeabcdefghijklm"))

    a = []
    print(longest_substring_in_order("efghijklmnopopqefgabcdeabcdefghijklm"))
    print(longest_substring_in_order("x"))
    print(longest_substring_in_order("xxyzstuopqklmefgabc"))
    print(longest_substring_in_order("efghijklmnopopqefgabcdeabcdefghijklm"))
    print(longest_substring_in_order("abcdefghijk"))
    print(longest_substring_in_order(""))
    print(longest_substring_in_order("zyxtr"))
    print(a)
main()
