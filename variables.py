#assigning variables and asking the user to input their name.
name = input('Enter your name here: ')
print(name)


#Switching variables
a = input("a: ")
b = input("b: ")


####################################
#Write your code below this line 👇
c = a #find a third variable and store the first item in it and do the swapping with the other variable
a = b
b = c

####################################
print("a: " + a)
print("b: " + b)
