#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
welcome_message = "Welcome to the tip calculator"
print(welcome_message)
total_bill = input("What was the total bill? $")
total_bill_as_int = int(total_bill)
tip_percentage = input(
    f"What percentage tip would you like to give? 10, 12, or 15?")
tip_percentage_as_int = int(tip_percentage)
new_tip_percentage = (tip_percentage_as_int / 100)
no_of_people = input("How many people to split the bill?")
no_of_people_as_int = int(no_of_people)
tip = float(total_bill_as_int * new_tip_percentage)
total_bill_plus_tip = float(total_bill_as_int + tip)
each_person_bill = float(total_bill_plus_tip / no_of_people_as_int)
each_person_bill_final = "{:.2f}".format(each_person_bill)
print(f"Each person should pay: ${each_person_bill_final}")
