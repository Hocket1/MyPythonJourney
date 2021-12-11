# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

#Where x, y and z are replaced with the actual calculated numbers.

print('Welcome to my life in weeks Program')
user_age = input(str('Enter your current age here: \n'))
number_of_days_in_year = 365
number_of_months_in_year = 12
number_of_weeks_in_year = 52
age_limit = 90
age_to_live = age_limit - int(user_age)
number_of_days_to_live = age_to_live * number_of_days_in_year
number_of_weeks_to_live = age_to_live * number_of_weeks_in_year
number_of_months_to_live = age_to_live * number_of_months_in_year
print(f'You have {number_of_days_to_live} days, {number_of_weeks_to_live} weeks, and {number_of_months_to_live} months left.')
