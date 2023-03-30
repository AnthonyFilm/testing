# Question 1
# Write a function to print
# "hello_USERNAME!" USERNAME 
# is  the input of the 
# function. The first line of 
# the code has been defined as 
# below.

def hello_name(user_name):
	""" prints greeting to user """
	print("hello_"+user_name)
	
name = input("\nPlease enter your username. ")
print()
hello_name(name)
print()

# Question 2
# Write a python function, 
# first_odds that prints the 
# odd numbers from 1-100 and 
# returns nothing

def first_odds():
	""" generates first odd numbers less than 100 """
	for num in range(100):
		if num % 2 == 1:
			print(num, end=" ")
print()
print("Here are the first odd numbers less than 100. ")
print(first_odds())
print()

# Question 3
# Please write a Python function, 
# max_num_in_list to return the max 
# number of a given list.

def max_num_in_list(a_list):
	"""returns maximum number in a list of numbers, excludes strings"""
	temp_max = a_list[0]
	for value in a_list:
		if type(value) == str:
			continue
		if value > temp_max:
			temp_max = value
	return temp_max


my_list = [1, 44, 20, 4, 5]
print("Here is a list of numbers")
print(my_list)
print("This is the highest number in that list:")
print(max_num_in_list(my_list))
print()

# Question 4
# Write a function to return if the given year 
# is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also 
# divisible by 400. 
# The return should be boolean Type (true/false).


def is_leap_year(a_year):	
	""" tests if a given year is a leap year. """
	if a_year % 4 == 0 and (not(a_year % 100 == 0)):
		return True
	elif a_year % 400 == 0:
		return True
	else:
		return False


while True:	
	your_year = input("Enter a year and I will tell you whether it's a leap year: ")
	if str.isalpha(your_year):
			print("This isn't ancient Rome. There are no letters in years. Please enter a year expressed as a proper Arabic number.")
			continue
	your_year = int(your_year)
	if is_leap_year(your_year):
			print(str(your_year)+" is a leap year.")
	else:
			print(str(your_year)+" is not a leap year.")
	again = input("Do you want to enter another year? Enter Y. If not, enter N: ")
	if again.lower() == "n":
			print()
			break
	else:
			continue

# Question 5
# Write a function to check to see if all 
# numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
	"""checks to see if list of numbers is consecutive """
	i = 0
	while i in range(len(a_list) - 1):
		if a_list[i] == a_list[i + 1] - 1:
			i += 1
			continue
		else:
			return False
	return True

print("Here is a list of numbers:")
my_num_list = [1,2, 3, 4, 5, 6, 7]
print(my_num_list)
if (is_consecutive(my_num_list)):
	print("These are consecutive numbers.")
else:
	print("These are NOT consecutive numbers.")
