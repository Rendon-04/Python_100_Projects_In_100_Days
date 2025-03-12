print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))




# find the tip amount of by dividing the tip amount by 100 and then multiplied by the total of the bill
total_tip = (tip / 100) * bill
# find the total amount of the bill by adding the total bill plus the total tip amount
total_amount = bill + total_tip
# find the amount each person should pay
each_person_pay = total_amount / people
print(total_tip)
print(total_amount)

final_amount= float(each_person_pay)
print(f"Each person should pay: {final_amount}")
