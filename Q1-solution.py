import math 


def get_sum_factorial_number_digits(number_input):
	number_factorial = math.factorial(number_input)

	list_digit = [int(x) for x in str(number_factorial)]

	print('Your sum of digits of factorial is : ' + str(sum(list_digit)))
	
get_sum_factorial_number_digits(100)
