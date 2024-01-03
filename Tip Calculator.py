#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

#Input the total bill, tip, and number of people to split the bill with
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

#Convert all variables so that it is easier to calculate how much each person should pay
bill2 = float(bill)
tip2 = int(tip)
people2 = int(people)

#Determine the tip amount based on the percent tipped
tip_percent = tip2 / 100
tip_amount = bill2 * tip_percent

#Total bill is the total bill plus the tip given
total_bill = bill2 + tip_amount

#Bill per person is the total bill divided by the number of people
bill_per_person = total_bill / people2

#Final amount is the bill per person rounded to 2 decimal places
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

#Each person will need to pay this amount
print(f"Each person should pay: ${final_amount}")
