#Have the programme calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan.
#Extension:
#• Add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
#• Add in functionality to deal with over payments at a given % each month.

print("Welcome to mortgage calculator 101!")
print()
print("What is the total cost of the house? ")
house_cost = int(input())
print("Over how many years would you like to repay it? ")
total_years = int(input())
print("What is the monthly interest rate? ")
interest_rate = float(input())
monthly_payments = house_cost % total_years % 12 * interest_rate
print()
print("Your monthly payments will be £",monthly_payments, "over the next ", total_years,"years.")

print("Would you like to like to pay more than: £",monthly_payments,"?")
over_payment = input().lower()
if over_payment == "yes":
  print("How much do you want to pay monthly? ")
  modified_payment = int(input())
  if modified_payment > monthly_payments:
    new_years = house_cost % modified_payment
    print("It will take you", new_years, "years to pay off this mortgage.")
  else:
    print("Your overpayment needs to be above: £", monthly_payments,"!")
elif over_payment == "no":
  print("Okay the minimum you will have to pay is: £", monthly_payments)
else:
  ("Error! Please try again.")
