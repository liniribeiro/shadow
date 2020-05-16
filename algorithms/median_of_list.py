
def format_n(number):
    precision = 1
    return"{:.{}f}".format(number, precision)


def running_median(a):
    processed_list = []
    result_list = []
    for number in a:
        processed_list.append(number)
        processed_list.sort()

        is_odd = len(processed_list) % 2 != 0
        middle = float(len(processed_list)) / 2

        if is_odd:
            result = processed_list[int(middle - .5)]
            result_list.append(format_n(result))
        else:
            sum = processed_list[int(middle)] + processed_list[int(middle - 1)]
            result = sum / 2
            result_list.append(format_n(result))

    return result_list


if __name__ == "__main__":
    s = [37632, 10118, 25334, 84618, 87339, 97852, 91683, 99232, 31552, 90453]

    pr = running_median(s)
    print(f">>>>>{pr}")
