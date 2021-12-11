print("Welcome to my tip calcualtor")
bill = float(input("Enter the bill here: \n"))
tip = input("Enter how much you would like to give? 10, 12, or 15? \n")
people = int(input("Enter the number of people you would like to split the bill to here: \n"))
tip_as_percent = int(tip)/100
Total_tip_amount = bill * tip_as_percent
total_bill_amount = Total_tip_amount + bill
bill_per_person = total_bill_amount/people
each_person = round(bill_per_person, 2)
print(each_person)
