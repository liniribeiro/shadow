from random import randint


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


for mciNumbers in range(0,3):
	print('55', random_with_N_digits(11))