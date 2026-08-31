def digit_root(num):
    root = num
    while len(str(root)) > 1:
        summ = 0
        for str_digit in str(root):
            summ += int(str_digit)
        root = summ
    return root


print(digit_root(889987))