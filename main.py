#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
itb = float(total_bill)
percentage_tip = input("What percentage tip would you like to give? 10, 12, 15 (Please do not add %) ")
ipt = float(percentage_tip)
number_ppl= input("How many people to split the bill? ")
inp = float(number_ppl)
p = (itb * ipt/100)
total_to_pay = (itb + p)
amount_per_person = total_to_pay/inp
app = round(amount_per_person, 2)
app = "{:.2f}".format(amount_per_person)
print(f"Each person should pay ${app}")